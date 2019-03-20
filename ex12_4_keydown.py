import sys
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption("Test KeyDown")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(str(event.key))


main()