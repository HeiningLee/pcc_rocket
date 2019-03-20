import pygame


class Rocket():
    def __init__(self, screen):

        # To get a screen and it's rect
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # To get an image and it's rect
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()

        # To define the location of the rocket by it's rect, and by the screen
        # rect.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # rocket movement flag
        self.moving_down = False
        self.moving_up = False
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, settings):
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.centery += settings.rocket_speed_factor
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.centery -= settings.rocket_speed_factor
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.centerx -= settings.rocket_speed_factor
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.centerx += settings.rocket_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

