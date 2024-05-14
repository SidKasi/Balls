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

#base parameters
maxRad = 30
gravity = np.array([0, -9.8])
drag = 0.9


balls = [Ball(rand.randint(5, maxRad),[rand.randint(maxRad, width - maxRad), rand.randint(maxRad, height - maxRad)], [rand.randint(0,3), rand.randint(0, 3)], [0, 0], (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))) for _ in range(100)]

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
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

    clock.tick(120)
