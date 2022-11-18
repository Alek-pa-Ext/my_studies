import pygame
import random
from In import In, Explosion
from Corvette import Corvette
from Frigate import Frigate
from Cruiser import Cruiser
from Heavycruiser import Heavycruiser
from StarDestroyer import StarDestroyer
from Battlecruiser import Battlecruiser
from Dreadnaughts import Dreadnaughts


dict_ships = {1: Corvette, 2: Frigate, 3: Cruiser, 4: Heavycruiser,
              5: StarDestroyer, 6: Battlecruiser, 7: Dreadnaughts}


# Game loop.
pygame.mixer.music.play(loops=-1)
running = True
game_over = True
while running:
    if game_over:
        In.show_go_screen()
        game_over = False
        score = 0
        In.shield = 100
        all_sprites = pygame.sprite.Group()
        # We create ships.
        ships = [dict_ships[i]() for i in dict_ships]
        # all_sprites.add(ships)
        all_sprites.add(ships)

    # We keep the cycle at the correct speed.
    In.clock.tick(In.FPS)
    # Process (event) input.
    for event in pygame.event.get():
        # Check window closure.
        if event.type == pygame.QUIT:
            running = False
        # Processing mouse clicks.
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create explosions at the location of the shots.
            In.shoot_sound.play()
            expl = Explosion(event.pos)
            all_sprites.add(expl)
            # We check the presence of ships at the site of the explosions.
            hits = pygame.sprite.spritecollide(expl, ships, False)
            for hit in hits:
                # We kill ships.
                if hit.damage(50):
                    score += hit.power
                    ships.remove(hit)
                    # Create a new one in place of the killed ship.
                    ships.append(dict_ships[random.randint(1, 7)]())
                    all_sprites.add(ships)

    # Update.
    all_sprites.update()
    In.screen.fill(In.BLACK)
    # Score.
    In.draw_text(In.screen, str(score), 18, In.WIDTH / 2, 10)
    # Health.
    In.draw_shield_bar(In.screen, 5, 5, In.shield)
    if In.shield < 1:
        game_over = True
    all_sprites.draw(In.screen)
    # After drawing everything, flip the screen.
    pygame.display.flip()
