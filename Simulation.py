import pygame
import sys
import random
from Cat import Cat
from Mouse import Mouse

# Grid size
N, P = 55, 55
CELL_SIZE = 10
WIDTH, HEIGHT = P * CELL_SIZE, N * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
CAT_COLOR = (255, 100, 100)
MOUSE_COLOR = (100, 100, 255)
TEXT_COLOR = (0, 0, 0)
WIN_COLOR = (0, 200, 0)

# Game settings
NUM_CATS = 3
NUM_MICE = 3

NUM_OBSTACLES = 50  # You can change this

obstacles = set()

# Pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 40))
pygame.display.set_caption("Cats vs Mice with Pathfinding")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Create multiple cats and mice
cats = []
mice = []

occupied = set()

# Place cats
for _ in range(NUM_CATS):
    while True:
        r, c = random.randint(0, N - 1), random.randint(0, P - 1)
        if (r, c) not in occupied:
            cats.append(Cat(r, c))
            occupied.add((r, c))
            break

# Place mice
for _ in range(NUM_MICE):
    while True:
        r, c = random.randint(0, N - 1), random.randint(0, P - 1)
        if (r, c) not in occupied:
            mice.append(Mouse(r, c))
            occupied.add((r, c))
            break

while len(obstacles) < NUM_OBSTACLES:
    r, c = random.randint(0, N - 1), random.randint(0, P - 1)
    if (r, c) not in occupied:
        obstacles.add((r, c))
        occupied.add((r, c))

turns = 0
game_won = False

def draw_grid():
    for row in range(N):
        for col in range(P):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_objects():
    for cat in cats:
        row, col = cat.get_position()
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, CAT_COLOR, rect)

    for mouse in mice:
        row, col = mouse.get_position()
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, MOUSE_COLOR, rect)

    for (row, col) in obstacles:
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (50, 50, 50), rect)  # Dark gray blocks

def draw_turn_count():
    text = font.render(f"Turn: {turns}", True, TEXT_COLOR)
    screen.blit(text, (10, HEIGHT + 10))

def draw_win_message():
    text = font.render("YOU WIN!", True, WIN_COLOR)
    screen.blit(text, (WIDTH // 2 - 60, HEIGHT + 10))


while True:
    screen.fill(WHITE)
    draw_grid()
    draw_objects()
    draw_turn_count()

    if game_won:
        font = pygame.font.Font(None, 72)
        text = font.render("You Win!", True, (0, 255, 0))
        #screen.blit(text, (N * GRID_SIZE // 3, P * GRID_SIZE // 3))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    # Wait for any key to advance turn
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Have each cat chase a mouse (if not already assigned)
    for cat in cats:
        cat.chase_mouse(mice, N, P, obstacles)

    # Remove caught mice
    cat_positions = {cat.get_position() for cat in cats}
    mice = [m for m in mice if m.get_position() not in cat_positions]

    # Move mice away from cats
    for mouse in mice:
        mouse.move_random(N, P, obstacles)

    # Remove any mice caught by cats after movement
    cat_positions = {cat.get_position() for cat in cats}
    mice = [m for m in mice if m.get_position() not in cat_positions]

    turns += 1

    if not mice:
        game_won = True

    clock.tick(10)