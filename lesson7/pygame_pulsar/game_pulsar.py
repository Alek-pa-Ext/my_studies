import pygame, sys, math
from rect_pulsar import Rectangle

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Second Game')
    back_color = (30,144,255)

    speed = 1
    widht = 50
    height = 50
    pulsar_count = 0
    pulsar_step = 10

    rectangle = Rectangle(screen, widht, height)

    clock = pygame.time.Clock()
    FPS = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(back_color)
        rectangle.output()

        pygame.display.update()

        clock.tick(FPS)

        if -pulsar_step <= pulsar_count <= pulsar_step:
            rectangle.rec.width += pulsar_count
            rectangle.rec.height += pulsar_count
            rectangle.rec.center = rectangle.screen_rect.center
            pulsar_count += speed
        else:
            speed = - speed
            pulsar_count = -pulsar_step * speed / abs(speed)


if __name__ == "__main__":
    run()


