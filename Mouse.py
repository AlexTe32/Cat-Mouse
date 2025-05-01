import random

class Mouse:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.assigned = False

    def get_position(self):
        return self.row, self.col

    def is_assigned(self):
        return self.assigned

    def assign_to_cat(self, cat):
        self.assigned = True

    def unassign(self):
        self.assigned = False

    def manhattan(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def move_random(self, max_rows, max_cols, obstacles=set(), occupied=set()):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        random.shuffle(directions)
        for direction in directions:
            r, c = self.row, self.col
            new_r, new_c = r, c
            if direction == 'UP' and r > 0:
                new_r -= 1
            elif direction == 'DOWN' and r < max_rows - 1:
                new_r += 1
            elif direction == 'LEFT' and c > 0:
                new_c -= 1
            elif direction == 'RIGHT' and c < max_cols - 1:
                new_c += 1
            if (new_r, new_c) not in obstacles and (new_r, new_c) not in occupied:
                self.row, self.col = new_r, new_c
                break

    def move_away_from_cats(self, cats, grid_rows, grid_cols, obstacles=set(), occupied=set()):
        if not cats:
            return

        my_pos = self.get_position()
        nearest_cat = min(cats, key=lambda c: self.manhattan(my_pos, c.get_position()))
        danger_pos = nearest_cat.get_position()

        best_move = my_pos
        best_dist = self.manhattan(my_pos, danger_pos)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = self.row + dr
            new_c = self.col + dc
            new_pos = (new_r, new_c)
            if (
                0 <= new_r < grid_rows and
                0 <= new_c < grid_cols and
                new_pos not in obstacles and
                new_pos not in occupied
            ):
                dist = self.manhattan(new_pos, danger_pos)
                if dist > best_dist:
                    best_dist = dist
                    best_move = new_pos

        self.row, self.col = best_move
