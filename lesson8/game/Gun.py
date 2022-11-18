import pygame


class Gun():


    def __init__(self, screen):
        self.screen = screen
        self.damage = 10
        self.img = pygame.image.load('../images/gun.png')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.y = self.screen.get_height() - self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def move(self, x):
        if self.rect.width / 2 <= x <= (self.screen.get_width() - self.rect.width / 2):
            self.rect.centerx = x
