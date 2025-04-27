# player.py
import pygame
from settings import TILE, YELLOW
from maze import can_move, eat_dot

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = (0, 0)
        self.score = 0

    def handle_input(self, key):
        if key == pygame.K_LEFT: self.dir = (-1, 0)
        elif key == pygame.K_RIGHT: self.dir = (1, 0)
        elif key == pygame.K_UP: self.dir = (0, -1)
        elif key == pygame.K_DOWN: self.dir = (0, 1)

    def update(self):
        next_x = self.x + self.dir[0]
        next_y = self.y + self.dir[1]
        if can_move(next_x, next_y):
            self.x = next_x
            self.y = next_y
        self.score += eat_dot(self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x*TILE+TILE//2, self.y*TILE+TILE//2), TILE//2 - 2)
