import pygame, sys
from Ships import CapitalShip
from pygame.sprite import Group
import random
from gun import Gun

def run():

    """Create screen"""
    pygame.init()
    screen = pygame.display.set_mode((1500, 700))
    pygame.display.set_caption('StarShipDestroyer')
    back_img = pygame.image.load('C:\\-\\my_studies\\lesson8\\images\\bg_img-space.png')

    """Set time"""
    FPS = 30
    fpsClock = pygame.time.Clock()

    """Set first settings for ships"""
    ships = Group()
    UEVENT_SPAWN_SHIP = pygame.USEREVENT + 1
    pygame.time.set_timer(UEVENT_SPAWN_SHIP, 3000)
    ships.add(CapitalShip(screen, random.randrange(10, screen.get_height() - 200, 128)))

    gun = Gun(screen)
    lifes = 10

    """Main cycle"""
    while True:
        """Events handler"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == UEVENT_SPAWN_SHIP:  # Spawn ships
                new_ship = CapitalShip(screen, random.randrange(10, screen.get_height() - 200, 128))
                ships.add(new_ship)

        screen.blit(back_img, (0, 0))  # Set background

        ships.update()  # Update group
        gun.draw()


        """Act ships"""
        for ship in ships.sprites():
            ship.draw()
            ship.move()
            if ship.hp <= 0:
                ships.remove(ship)
            if ship.rect.x <= 0:
                ships.remove(ship)
                lifes -= ship.power

        print(lifes)
        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    run()