import pygame, sys
from rect import Rectangle

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('First Game')
    back_color = (30,144,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(back_color)

        rectangle = Rectangle(screen)
        rectangle.output()

        pygame.display.flip()



if __name__ == "__main__":
    run()



