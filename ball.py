import numpy as np
import pygame as pg
import math

class Ball:
    def __init__(self, radius, x = [0, 0], v = [0, 0], a = [0, 0], color = (255, 0, 0)):
        self.r = radius
        self.color = color
        self.x = np.array(x)
        self.v = np.array(v)
        self.a = np.array(a)

    def render(self, screen):
        pg.draw.circle(screen, self.color, self.x, self.r)

    def collide(self, width, height, balls):

        if self.x[0] - self.r <= 0:
            self.x[0] += self.r
            self.v[0] = -self.v[0]
        if self.x[0] + self.r >= width:
            self.x[0] -= self.r
            self.v[0] = -self.v[0]
        if self.x[1] - self.r <= 0:
            self.x[1] += self.r
            self.v[1] = -self.v[1]
        if self.x[1] + self.r >= height:
            self.x[1] -= self.r
            self.v[1] = -self.v[1]


        for ball in balls:
            disp = self.x - ball.x

            if np.sum(disp**2) <= (self.r + ball.r)**2:
                #impact = 2 * ball.r ** 2 / (self.r ** 2 + ball.r ** 2) * np.dot(delta_v, disp) / np.dot(disp, disp)
                correction = ((self.r + ball.r - np.linalg.norm(disp)) * disp/np.linalg.norm(disp) * 1).astype(int)
                self.x += correction
                ball.x -= correction

                self.v[0] = -self.v[0]
                self.v[1] = -self.v[1]
                ball.v[0] = -ball.v[0]
                ball.v[1] = -ball.v[1]
    def update(self):
            self.x += self.v
            self.v += self.a



