import pygame
import sys


def manage_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1


def draw_screen(screen, ship, bg_color):
    screen.fill(bg_color)
    ship.draw()
    pygame.display.flip()
