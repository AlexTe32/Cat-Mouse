from pathfinding import a_star, manhattan
class Cat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.target_mouse = None  # This will store the assigned mouse

    def get_position(self):
        return self.row, self.col

    def set_target_mouse(self, mice):
        # Find the nearest unassigned mouse
        min_distance = float('inf')
        nearest_mouse = None
        for mouse in mice:
            if mouse.is_assigned():
                continue
            dist = abs(self.row - mouse.row) + abs(self.col - mouse.col)
            if dist < min_distance:
                min_distance = dist
                nearest_mouse = mouse

        if nearest_mouse:
            self.target_mouse = nearest_mouse
            nearest_mouse.assign_to_cat(self)

    def move_toward_mouse(self, grid_rows, grid_cols, obstacles=set()):
        if self.target_mouse is None:
            return  # No mouse to chase

        my_pos = self.get_position()
        target_pos = self.target_mouse.get_position()

        # Use A* pathfinding to move toward the mouse
        path = a_star(my_pos, target_pos, grid_rows, grid_cols, obstacles)

        if path:
            self.row, self.col = path[0]

    def chase_mouse(self, mice, grid_rows, grid_cols, obstacles=set()):
        # Assign target mouse only if none assigned
        if not self.target_mouse:
            self.set_target_mouse(mice)

        # Move towards the assigned mouse
        self.move_toward_mouse(grid_rows, grid_cols, obstacles)
