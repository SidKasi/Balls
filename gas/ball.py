import numpy as np
import pygame as pg

# impact = 2 * ball.r ** 2 / (self.r ** 2 + ball.r ** 2) * np.dot(delta_v, disp) / np.dot(disp, disp)


class Ball:
    def __init__(self, radius, x = [0.0, 0.0], v = [0.0, 0.0], a = [0.0, 0.0], color = (255, 0, 0)):
        self.r = radius
        self.color = color
        self.x = np.array(x)
        self.v = np.array(v)
        self.a = np.array(a)
    def render(self, screen):
        pg.draw.circle(screen, self.color, self.x, self.r)

    def collide(self, width, height, balls):

        if self.x[0] - self.r <= 0:
            self.x[0] += self.r - self.x[0]
            self.v[0] = -self.v[0]
        if self.x[0] + self.r >= width:
            self.x[0] -= self.r - (width - self.x[0])
            self.v[0] = -self.v[0]
        if self.x[1] - self.r <= 0:
            self.x[1] += self.r - self.x[1]
            self.v[1] = -self.v[1]
        if self.x[1] + self.r >= height:
            self.x[1] -= self.r - (height - self.x[1])
            self.v[1] = -self.v[1]


        for ball in balls:
            disp = self.x - ball.x

            #if (self.x[0] - ball.x[0])**2 + (self.x[1] - ball.x[1])**2 <= (self.r + ball.r)**2:
            if np.sum(disp**2) <= (self.r + ball.r)**2:

                axis = (disp/np.linalg.norm(disp))
                tangent = np.array([[0, -1], [1, 0]]) @ axis # multiply by rotation matrix

                correction = ((self.r + ball.r - np.linalg.norm(disp)) * axis * 0.5)
                self.x += correction
                ball.x -= correction

                mSelf, mBall = self.r**2, ball.r**2
                selfNormVi, ballNormVi = np.dot(axis, self.v), np.dot(axis, ball.v)
                selfTanV, ballTanV = np.dot(tangent, self.v), np.dot(tangent, ball.v)

                selfNormVf = ((mSelf - mBall) * selfNormVi + 2 * mBall * ballNormVi)/(mSelf + mBall)
                ballNormVf = ((mBall - mSelf) * ballNormVi + 2 * mSelf * selfNormVi)/(mSelf + mBall)

                self.v = np.array([selfNormVf * axis[0] + selfTanV * tangent[0], selfNormVf * axis[1] + selfTanV * tangent[1]])
                ball.v = np.array([ballNormVf * axis[0] + ballTanV * tangent[0], ballNormVf * axis[1] + ballTanV * tangent[1]])
    def update(self):
            self.x += self.v
            self.v += self.a


