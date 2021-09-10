import pygame

from robot import Robot

from pygame.locals import (K_ESCAPE,
                           KEYDOWN)
                

pygame.init()
vec = pygame.math.Vector2

FPS = 60
SCREEN_WIDTH_HEIGHT = (800, 600)

# setup drawing window
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
pygame.display.set_caption("Robot Simulator")

running = True


robot = Robot((0,0), 2, (0,0))
robot.set_position((0,0))

all_sprites = pygame.sprite.Group()

all_sprites.add(robot)

while running:

    # Did user click window close button
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    robot.go_to((250, 250))


    screen.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()