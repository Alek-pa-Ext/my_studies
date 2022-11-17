import pygame, sys
from Ships import CapitalShip, MiddleShip, SmallShip
from pygame.sprite import Group
import random
from gun import Gun
from bullet import Bullet
from scores import Scores
from pause import Stop

def run():

    """Create screen"""
    pygame.init()
    screen = pygame.display.set_mode((1500, 700))
    pygame.display.set_caption('StarShipDestroyer')
    back_img = pygame.image.load('..\\images\\bg_img-space.png')

    """Set time"""
    FPS = 30
    fpsClock = pygame.time.Clock()


    """Set event's settinds"""
    SPAWN_CAPITAL_SHIP = pygame.USEREVENT + 1
    SPAWN_MIDDLE_SHIP = pygame.USEREVENT + 2
    SPAWN_SMALL_SHIP = pygame.USEREVENT + 3
    DIFFICULT_UP = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_CAPITAL_SHIP, 10000)
    pygame.time.set_timer(SPAWN_MIDDLE_SHIP, 5000)
    pygame.time.set_timer(SPAWN_SMALL_SHIP, 3000)
    pygame.time.set_timer(DIFFICULT_UP, 10000)

    difficult = 10
    stop = Stop(screen)

    gun = Gun(screen)
    bullets = Group()
    ships = Group()
    ships.add(CapitalShip(screen, random.randrange(30, screen.get_height() - 200, 128), difficult))

    life = Scores(screen, 'Life', 10, 0)
    score = Scores(screen, 'Score', 0, 1)

    while True:
        """Events handler"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SPAWN_CAPITAL_SHIP:
                new_ship = CapitalShip(screen, random.randrange(30, screen.get_height() - 200, 128), difficult)
                ships.add(new_ship)
            elif event.type == SPAWN_MIDDLE_SHIP:
                new_ship = MiddleShip(screen, random.randrange(30, screen.get_height() - 200, 128), difficult)
                ships.add(new_ship)
            elif event.type == SPAWN_SMALL_SHIP:
                new_ship = SmallShip(screen, random.randrange(30, screen.get_height() - 200, 128), difficult)
                ships.add(new_ship)
            elif event.type == DIFFICULT_UP:
                difficult += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_bullet = Bullet(screen, gun.rect.centerx - 5, gun.rect.top)
                bullets.add(new_bullet)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop.is_pause = True

        while stop.is_pause:
            """Events handler"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        stop.is_pause = False

            screen.blit(back_img, (0, 0))
            stop.draw_pause()
            life.draw()
            score.draw()
            pygame.display.flip()

        while stop.is_gameover:
            """Events handler"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if stop.rect.collidepoint(pygame.mouse.get_pos()):
                        stop.is_gameover = False
                        difficult = 10
                        life.stats = 10
                        score.stats = 0
                        ships.empty()
                        bullets.empty()
                        ships.add(CapitalShip(screen, random.randrange(30, screen.get_height() - 200, 128), difficult))
                        pygame.time.set_timer(SPAWN_CAPITAL_SHIP, 10000)
                        pygame.time.set_timer(SPAWN_MIDDLE_SHIP, 5000)
                        pygame.time.set_timer(SPAWN_SMALL_SHIP, 3000)
                        pygame.time.set_timer(DIFFICULT_UP, 10000)
            pygame.mouse.set_visible(True)
            screen.blit(back_img, (0, 0))
            stop.draw_gameover()
            life.draw()
            score.draw()
            pygame.display.flip()

        pygame.mouse.set_visible(False)
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
                life.stats = max(life.stats - ship.power, 0)
            collisions = pygame.sprite.groupcollide(ships, bullets, False, True)
            if collisions:
                for ship in collisions.keys():
                    ship.get_damage(gun.damage)

        life.draw()
        score.draw()
        if life.stats <= 0:
            stop.is_gameover = True

        gun.move(pygame.mouse.get_pos()[0])
        gun.draw()

        pygame.display.flip()
        fpsClock.tick(FPS)




if __name__ == "__main__":
    run()