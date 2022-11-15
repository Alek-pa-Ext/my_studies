import pygame, sys
from Ships import CapitalShip
from pygame.sprite import Group
import random
from gun import Gun
from bullet import Bullet

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
    bullets = Group()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_bullet = Bullet(screen, gun.rect.centerx - 5, gun.rect.top)
                bullets.add(new_bullet)




        screen.blit(back_img, (0, 0))  # Set background

        ships.update()  # Update group
        bullets.update()



        """Act bullets"""
        for bullet in bullets:
            bullet.draw()
            bullet.move()
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)


        gun.draw()

        """Act ships"""
        for ship in ships.sprites():
            ship.draw()
            ship.move()
            collisions = pygame.sprite.groupcollide(bullets, ships, True, False)
            if collisions:
                ship.get_damage(gun.damage)
            if ship.hp <= 0:
                ships.remove(ship)
            if ship.rect.x <= 0:
                ships.remove(ship)
                lifes -= ship.power


        gun.move(pygame.mouse.get_pos()[0])

        #print(len(bullets))
        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    run()