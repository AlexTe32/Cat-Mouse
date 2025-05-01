from pathfinding import a_star, manhattan

class Cat:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def move_toward_mouse(self, mice, grid_rows, grid_cols, obstacles=set(), occupied=set()):
        if not mice:
            return

        my_pos = self.get_position()

        # Find the nearest mouse by Manhattan distance
        nearest = min(mice, key=lambda m: manhattan(my_pos, m.get_position()))
        target_pos = nearest.get_position()

        # Compute A* path to the nearest mouse
        path = a_star(my_pos, target_pos, grid_rows, grid_cols, obstacles | occupied)

        # Move one step if path exists and is unoccupied
        if path and path[0] not in occupied:
            self.row, self.col = path[0]
