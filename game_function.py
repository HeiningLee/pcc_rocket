import sys
import pygame
from missile import Missile


def check_events(settings, screen, rocket, missiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, rocket, missiles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, settings, screen, rocket, missiles):
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_SPACE:
        if len(missiles) < settings.missiles_allowed:
            new_missile = Missile(settings, screen, rocket)
            missiles.add(new_missile)


def check_keyup_events(event, rocket):
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False


def update_screen(settings, screen, rocket, missiles):
    screen.fill(settings.bg_color)
    rocket.blitme()
    for missile in missiles.sprites():
        missile.showme()

    pygame.display.flip()


def manage_missiles(settings, screen, rocket, missiles):
    for missile in missiles.copy():
        if missile.rect.left > missile.screen_rect.right:
            missiles.remove(missile)
