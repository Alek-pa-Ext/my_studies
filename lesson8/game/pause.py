import pygame

class Stop():
    def __init__(self, screen):
        self.is_pause = False
        self.is_gameover = False
        self.screen = screen
        self.pause_img = pygame.image.load('..\\images\\pause.png')
        self.gameover_img = pygame.image.load('..\\images\\gameover.png')
        self.rect = self.pause_img.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.centery = self.screen.get_rect().centery


    def draw_pause(self):
        self.screen.blit(self.pause_img, self.rect)

    def draw_gameover(self):
        self.screen.blit(self.gameover_img, self.rect)