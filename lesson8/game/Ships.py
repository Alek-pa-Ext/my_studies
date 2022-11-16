import pygame


class CapitalShip(pygame.sprite.Sprite):

    def __init__(self, screen, y):
        super(CapitalShip, self).__init__()
        self.screen = screen
        self.speed = 2.5
        self.hp = 100
        self.power = 1
        self.anim_count = 0
        self.imgs = [pygame.image.load('C:\\-\\my_studies\\lesson8\\images\\1st-spaceship.png'),
                     pygame.image.load('C:\\-\\my_studies\\lesson8\\images\\1st-spaceship_1.png')]
        self.rect = self.imgs[self.anim_count].get_rect()
        self.rect.x = screen.get_rect().width
        self.rect.y = y

    def get_damage(self, damage):
        self.hp -= damage

    def draw(self):
        self.screen.blit(self.imgs[self.anim_count // 30], self.rect)

    def move(self):
        if self.rect.x > - self.rect.width:
            self.rect.x -= self.speed
            if self.anim_count + 1 < len(self.imgs) * 30:
                self.anim_count += 1
            else:
                self.anim_count = 0
        else:
            self.rect.x = 1500
            self.anim_count = 0

