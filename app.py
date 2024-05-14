import numpy as np
import pygame as pg
from ball import Ball
import random as rand

pg.init()
clock = pg.time.Clock()
# Screen dimensions and settings
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Ball")
maxRad = 15

balls = [Ball(rand.randint(maxRad, maxRad),[rand.randint(maxRad, width - maxRad), rand.randint(maxRad, height - maxRad)], [rand.randint(0,10), rand.randint(0, 10)], [0, 1], (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))) for _ in range(10)]

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == 32:
                #ball1.v += np.array([0, -10])
                pass
            else:
                running = False

    for i in range(len(balls)):
        ballsCopy = balls.copy()
        ballsCopy.pop(i)
        balls[i].collide(width, height, ballsCopy)

    for ball in balls:
        ball.update()

    screen.fill((0, 0, 0))

    for ball in balls:
        ball.render(screen)

    pg.display.flip()

    clock.tick(60)
