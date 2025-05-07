import pygame
import sys
import random
import time
from Cat import Cat
from Mouse import Mouse

# Самата симулација е дефинирана како функција
# Функцијата го прима бројот на мачки и глувци, големината, број на препреки, и време помеќу циклуси
def run_simulation(N=80, P=80, num_cats=3, num_mice=3, num_obstacles=150, wait_time=0):
    # Се дефинира големината на целија и големината на прозорецот
    CELL_SIZE = 10
    WIDTH, HEIGHT = P * CELL_SIZE, N * CELL_SIZE

    # Се дефинират разлицни бои за различни променливи
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    CAT_COLOR = (255, 100, 100)
    MOUSE_COLOR = (100, 100, 255)
    TEXT_COLOR = (0, 0, 0)
    WIN_COLOR = (0, 200, 0)

    # Иницијализирај pygame
    # Користиме pygame за да ни го олесни симулацијата и визулацијата
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 40))
    pygame.display.set_caption("Cat and Mouse")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    # Иницилизираме низи за Мачките, Глувците и Препреките
    cats = []
    mice = []
    occupied = set()
    obstacles = set()

    # Ги поставуваме сите елементи на случајни места и ги додаваме во содветните низи
    for _ in range(num_cats):
        while True:
            r, c = random.randint(0, N - 1), random.randint(0, P - 1)
            if (r, c) not in occupied:
                cats.append(Cat(r, c))
                occupied.add((r, c))
                break

    for _ in range(num_mice):
        while True:
            r, c = random.randint(0, N - 1), random.randint(0, P - 1)
            if (r, c) not in occupied:
                mice.append(Mouse(r, c))
                occupied.add((r, c))
                break

    while len(obstacles) < num_obstacles:
        r, c = random.randint(0, N - 1), random.randint(0, P - 1)
        if (r, c) not in occupied:
            obstacles.add((r, c))
            occupied.add((r, c))

    # Бидејчи секое движење е една секунда ги броиме потребните циклуси
    turns = 0

    # Дефинираме функцији за визуализација на елементите
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
            pygame.draw.rect(screen, (50, 50, 50), rect)

    def draw_turn_count():
        text = font.render(f"Turn: {turns}", True, TEXT_COLOR)
        screen.blit(text, (10, HEIGHT + 10))

    # Ова е главниот луп на симулацијата
    while True:
        screen.fill(WHITE)
        draw_grid()
        draw_objects()
        draw_turn_count()

        pygame.display.flip()

        # Се цека крај на симулацијата за да се затвори прозорот
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Цекање помеѓу циклуси
        time.sleep(wait_time/5000)

        # Мачикете се движат на секој 3 циклус кон најблискиут Глушеч
        #( Повеќе објацнување кај Мачките)
        if (turns % 3) == 0:
            new_cat_positions = set()
            for cat in cats:
                others = new_cat_positions | {c.get_position() for c in cats if c != cat}
                cat.move_toward_mouse(mice, N, P, obstacles, others)
                new_cat_positions.add(cat.get_position())

        # Проверка дали некој глушец дели позиција со Мачка, и него отстранување
        cat_positions = {cat.get_position() for cat in cats}
        mice = [m for m in mice if m.get_position() not in cat_positions]

        # Движење на глувците
        new_mouse_positions = set()
        for mouse in mice:
            others = new_mouse_positions | {m.get_position() for m in mice if m != mouse}
            mouse.move_random(N, P, obstacles, others)
            new_mouse_positions.add(mouse.get_position())

        cat_positions = {cat.get_position() for cat in cats}
        mice = [m for m in mice if m.get_position() not in cat_positions]

        # Инкрементација на циклуси
        turns += 1

        # Проверка дали сеуште има глувци, ако нема се врача бројот на циклуси
        if not mice or turns>12000:
            font_big = pygame.font.Font(None, 72)
            pygame.display.flip()
            time.sleep(wait_time)
            pygame.quit()
            return turns

        clock.tick(10)
