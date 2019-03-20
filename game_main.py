import pygame
import game_function as gf
from settings import Settings
from rocket import Rocket
from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_mode)
    pygame.display.set_caption("Rocket")
    rocket = Rocket(screen)
    missiles = Group()

    while True:
        gf.check_events(settings, screen, rocket, missiles)
        rocket.update(settings)
        missiles.update(settings)
        gf.update_screen(settings, screen, rocket, missiles)
        gf.manage_missiles(settings, screen, rocket, missiles)

        print(len(missiles))


run_game()
