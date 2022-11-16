import pygame, sys
from Ships import CapitalShip
from pygame.sprite import Group
import random
from gun import Gun
from bullet import Bullet
from scores import Scores

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
    life = Scores(screen, 'Life', 3, 0)
    score = Scores(screen, 'Score', 0, 1)

    """Main cycle"""
    while True:
        """Events handler"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == UEVENT_SPAWN_SHIP:  # Spawn ships
                new_ship = CapitalShip(screen, random.randrange(30, screen.get_height() - 200, 128))
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




        """Act ships"""
        for ship in ships.sprites():
            ship.draw()
            ship.move()
            if ship.hp <= 0:
                ships.remove(ship)
                score.stats += ship.cost
            if ship.rect.x <= 0:
                ships.remove(ship)
                life.stats -= ship.power
            collisions = pygame.sprite.groupcollide(ships, bullets, False, True)
            if collisions:
                for ship in collisions.keys():
                    ship.get_damage(gun.damage)

        life.draw()
        score.draw()


        gun.move(pygame.mouse.get_pos()[0])
        gun.draw()

        #print(len(bullets))
        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    run()