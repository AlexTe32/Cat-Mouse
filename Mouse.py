import random
class Mouse:
    # Иницализација на Глушецот
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def move_random(self, max_rows, max_cols, obstacles=set(), occupied=set()):
        # Глушецот пробува да најде случајна позиција на која може да се помести
        # Ако прват позиција не е слободна ќе продолжи да тражи додека ненајде
        tried = set()
        while len(tried) < 4:
            direction = random.randint(0, 3)
            if direction in tried:
                continue
            tried.add(direction)

            new_r, new_c = self.row, self.col
            if direction == 0 and self.row > 0:
                new_r -= 1
            elif direction == 1 and self.row < max_rows - 1:
                new_r += 1
            elif direction == 2 and self.col > 0:
                new_c -= 1
            elif direction == 3 and self.col < max_cols - 1:
                new_c += 1

            # Кога ќе најде слободна позиција се поместува на неаА
            if (new_r, new_c) not in obstacles and (new_r, new_c) not in occupied:
                self.row, self.col = new_r, new_c
                break
