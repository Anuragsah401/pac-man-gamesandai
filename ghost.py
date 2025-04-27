# ghost.py
import pygame
import heapq
from settings import TILE, RED
from maze import can_move

class Ghost:
    def __init__(self, x, y, color=RED):
        self.x = x
        self.y = y
        self.color = color
        self.path = []

    def update(self, player):
        if not self.path or (self.x, self.y) == self.path[0]:
            self.path = astar((self.x, self.y), (player.x, player.y))

        if self.path:
            next_pos = self.path.pop(0)
            self.x, self.y = next_pos

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x*TILE+TILE//2, self.y*TILE+TILE//2), TILE//2 - 2)

    def check_collision(self, player):
        return self.x == player.x and self.y == player.y

def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not can_move(neighbor[0], neighbor[1]):
                continue

            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # no path found

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path[1:]  # skip current position
