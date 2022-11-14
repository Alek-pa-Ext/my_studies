import pygame, sys
from Ships import CapitalShip
from pygame.sprite import Group
import random

def run():

    """create screen"""
    pygame.init()
    screen = pygame.display.set_mode((1500, 700))
    pygame.display.set_caption('StarShipDestroyer')
    back_img = pygame.image.load('C:\\-\\my_studies\\lesson8\\images\\bg_img-space.png')

    """set time"""
    FPS = 30
    fpsClock = pygame.time.Clock()

    """set first settings for ships"""
    ships = Group()
    UEVENT_SPAWN_SHIP = pygame.USEREVENT + 1
    pygame.time.set_timer(UEVENT_SPAWN_SHIP, 3000)
    ships.add(CapitalShip(screen, random.randrange(10, screen.get_height() - 200, 128)))

    """main cycle"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == UEVENT_SPAWN_SHIP:
                new_ship = CapitalShip(screen, random.randrange(10, screen.get_height() - 200, 128))
                ships.add(new_ship)

        screen.blit(back_img, (0, 0))

        ships.update()

        for ship in ships.sprites():
            ship.draw(screen)
            ship.move()

        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    run()