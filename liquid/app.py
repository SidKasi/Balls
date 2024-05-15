import numpy as np
import pygame as pg
from ball import Ball
import random as rand

pg.init()
clock = pg.time.Clock()
# Screen dimensions and settings
width, height = 1600, 900
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Gas")

#base parameters
maxRad = 30
maxVel = 5
shrinking = False

balls = [Ball(rand.randint(10, maxRad),[rand.randint(maxRad, width - maxRad) * 1.0, rand.randint(maxRad, height - maxRad) * 1.0], [rand.randint(-maxVel,maxVel) * 1.0, rand.randint(1, 1) * 1.0], [0.0, 0.0], (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))) for _ in range(200)]

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if pg.mouse.get_pressed:
            print("pressed")
            cursor = pg.mouse.get_pos()
            for ball in balls:
                ball.a = (np.array(cursor) - ball.x) * 0.0001
        else:
            for ball in balls:
                ball.a = 0


    if shrinking:
        width -= 0.1
        height -= 0.1
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

    clock.tick(200)
