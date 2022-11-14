import pygame


class Gun():


    def __init__(self, screen):
        self.screen = screen
        self.damage = 50
        self.img = pygame.image.load('C:\\-\\my_studies\\lesson8\\images\\1st-spaceship.png')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.y = self.screen.get_rect().height - self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)