# main.py
import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, BLACK, WHITE, RED
from player import Player
from ghost import Ghost
from maze import draw_maze

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man with Ghosts")
clock = pygame.time.Clock()

# Entities
player = Player(14, 23)
ghost = Ghost(13, 15)

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player.handle_input(event.key)

    # Updates
    player.update()
    ghost.update(player)


    # Collision
    if ghost.check_collision(player):
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Draw
    draw_maze(screen)
    player.draw(screen)
    ghost.draw(screen)

    # Score
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 30))

    pygame.display.flip()

pygame.quit()
sys.exit()
