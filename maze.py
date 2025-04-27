# maze.py
from settings import TILE, BLUE, WHITE
import pygame

# 0: empty, 1: wall, 2: dot
maze = [
    [1]*28,
    [1]+[2]*26+[1],
    [1]+[2]*26+[1],
    [1]*28,
]

while len(maze) < 31:
    maze.append([1] + [2]*26 + [1])

def draw_maze(screen):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLUE, (x*TILE, y*TILE, TILE, TILE))
            elif cell == 2:
                pygame.draw.circle(screen, WHITE, (x*TILE+TILE//2, y*TILE+TILE//2), 3)

def can_move(x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[0]):
        return maze[y][x] != 1
    return False

def eat_dot(x, y):
    if maze[y][x] == 2:
        maze[y][x] = 0
        return 10
    return 0
