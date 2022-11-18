import pygame

class Rectangle:

    yellow = (225, 225, 0)

    def __init__(self, screen, wight, height):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rec = pygame.Rect(0, 0, wight, height)
        self.rec.center = self.screen_rect.center

    def output(self, color=yellow):
        pygame.draw.rect(self.screen, color, self.rec)

