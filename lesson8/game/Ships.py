import pygame


class CapitalShip(pygame.sprite.Sprite):

    def __init__(self, screen, y, difficult):
        super(CapitalShip, self).__init__()
        self.stats(difficult)
        self.screen = screen
        self.hp = self.max_hp
        self.anim_count = 0
        self.rect = self.imgs[self.anim_count].get_rect()
        self.rect.x = screen.get_rect().width
        self.rect.y = y
        self.x = float(self.rect.x)
        self.hp_rect = pygame.Rect(self.rect.x, self.rect.y - 20, self.rect.width, 5)
        self.hp_color = (78, 170, 53)

    def stats(self, difficult):
        self.speed = 2 * (difficult / 10)
        self.max_hp = 100
        self.power = 3
        self.cost = 10 * difficult
        self.imgs = [pygame.image.load('..\\images\\1st-spaceship.png'),
                     pygame.image.load('..\\images\\1st-spaceship_1.png')]


    def get_damage(self, damage):
        self.hp -= damage

    def draw(self):
        self.screen.blit(self.imgs[self.anim_count // 30], self.rect)
        pygame.draw.rect(self.screen, self.hp_color, self.hp_rect)

    def hp_bar_update(self):
        self.hp_rect.width = self.rect.width * (self.hp / self.max_hp)
        self.hp_rect.x = self.rect.x

    def move(self):
        if self.rect.x > - self.rect.width:
            self.x -= self.speed
            if self.anim_count + 1 < len(self.imgs) * 30:
                self.anim_count += 1
            else:
                self.anim_count = 0
        else:
            self.x = 1500
            self.anim_count = 0
        self.rect.x = self.x
        self.hp_bar_update()

class MiddleShip(CapitalShip):
    def stats(self, difficult):
        self.imgs = [pygame.image.load('..\\images\\2-spaceship_2.png'),
                     pygame.image.load('..\\images\\2-spaceship_3.png')]
        self.speed = 3 * (difficult / 10)
        self.max_hp = 50
        self.power = 2
        self.cost = 5 * difficult

class SmallShip(CapitalShip):
    def stats(self, difficult):
        self.imgs = [pygame.image.load('..\\images\\3-spaceship_1.png'),
                     pygame.image.load('..\\images\\3-spaceship_2.png')]
        self.speed = 5 * (difficult / 10)
        self.max_hp = 10
        self.power = 1
        self.cost = 1 * difficult