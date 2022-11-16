import pygame

class Scores():
    def __init__(self, screen, name_stats, stats, n):
        self.name_stats = name_stats
        self.stats = stats
        self.screen = screen
        self.text_color = (235, 229, 73)
        self.font = pygame.font.SysFont('appetite', 36)
        self.x = 20
        self.y = 20 + 40 * n
        self.update()

    def update(self):
        self.image = self.font.render(f'{self.name_stats}: {self.stats}', True, self.text_color)
        self.img_rect = self.image.get_rect()
        self.img_rect.y = self.y
        self.img_rect.x = self.x

    def draw(self):
        self.update()
        self.screen.blit(self.image, self.img_rect)
