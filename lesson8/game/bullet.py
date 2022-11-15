import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Bullet, self).__init__()
        self.color = (235, 229, 73)
        self.screen = screen
        self.rect = pygame.Rect(x, y, 10, 10)

    def move(self):
        self.rect.y -= 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
