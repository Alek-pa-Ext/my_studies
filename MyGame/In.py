import pygame
import os
import random


class In():

    # Orientation of the program on the disk.
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'res')

    # Colors (R, G, B)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    WIDTH = 800  # game window width
    HEIGHT = 600  # game window height
    FPS = 30  # frame rate per second

    # create a game and a window
    pygame.init()
    pygame.mixer.init()  # for sound
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Ship Destroyer")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    # loading sound
    shoot_sound = pygame.mixer.Sound(os.path.join(img_folder, 'pew.wav'))
    pygame.mixer.music.load(os.path.join(
        img_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)

    shield = 100

    def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, In.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, In.GREEN, fill_rect)
        pygame.draw.rect(surf, In.WHITE, outline_rect, 2)

    def show_go_screen():
        In.draw_text(
            In.screen,
            "Greetings, O warrior!",
            64, In.WIDTH / 2, In.HEIGHT / 4)
        In.draw_text(In.screen, "Press a mouse button to fire", 22,
                     In.WIDTH / 2, In.HEIGHT / 2)
        In.draw_text(In.screen, "Press a mouse button to begin",
                     18, In.WIDTH / 2, In.HEIGHT * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            In.clock.tick(In.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(
            In.img_folder, self.form)).convert()
        self.image = player_img
        self.image = pygame.transform.scale(
            self.image, (self.length, self.length))
        self.image.set_colorkey(In.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(
            self.length // 2, In.WIDTH - self.length // 2 + 1), 0)

    def update(self):
        self.rect.y += self.maximum_speed
        if self.rect.top > In.HEIGHT:
            self.rect.bottom = 0
            In.shield -= self.capacity


class Explosion(pygame.sprite.Sprite):

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        explosion_anim = Explosion.make_explosion_anim()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        explosion_anim = Explosion.make_explosion_anim()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    @staticmethod
    def make_explosion_anim():
        rez = []
        for i in range(9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pygame.image.load(os.path.join(
                In.img_folder, filename)).convert()
            img.set_colorkey(In.BLACK)
            img_lg = pygame.transform.scale(img, (75, 75))
            rez.append(img_lg)
        return rez
