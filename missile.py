import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    def __init__(self, settings, screen, rocket):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(settings.missile_image_path)
        self.rect = self.image.get_rect()

        self.x = float(rocket.rect.centerx)
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery - 10

    def update(self, settings):
        self.x += settings.missile_speed_factor
        self.rect.centerx = self.x

    def showme(self):
        self.screen.blit(self.image, self.rect)
