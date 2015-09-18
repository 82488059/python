# -*- coding:utf-8 -*-
from random import randint

import pygame
from pygame.locals import *

MAZE_MAX = 50
MOVE_RIGHT = (1, 0)
MOVE_LEFT = (-1, 0)
MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
direction = {0: {0: 0, 1: 1}, 1: {0: 1, 1: 0}, 2: {0: 0, 1: -1}, 3: {0: -1, 1: 0}}


class App(object):
    def __init__(self):
        self.map1 = {}
        for x in xrange(0, MAZE_MAX + 2):
            self.map1[x] = {}
            for y in xrange(0, MAZE_MAX + 2):
                self.map1[x][y] = 0
        pygame.init()
        screen_size = (640, 480)
        diamonds_size = (10, 10)
        self.screen = pygame.display.set_mode(screen_size, 0, 32)
        self.background = pygame.surface.Surface(screen_size).convert()
        self.diamonds1 = pygame.surface.Surface(diamonds_size).convert()
        self.diamonds2 = pygame.surface.Surface(diamonds_size).convert()
        self.diamonds3 = pygame.surface.Surface(diamonds_size).convert()
        self.red = pygame.surface.Surface(diamonds_size).convert()
        self.yellow = pygame.surface.Surface(diamonds_size).convert()
        self.background.fill((255, 255, 255))
        self.diamonds1.fill((128, 128, 128))
        self.diamonds2.fill((0, 0, 0))
        self.diamonds3.fill((0, 200, 0))
        self.red.fill((255, 0, 0))
        self.yellow.fill((255, 255, 0))
        self.x = 22
        self.y = 22
        self.end = (0, 0)
        self.begin = (0, 0)
        self.root = {}
        self.index = 0
        return

    def search(self, xx, yy):
        # self.render()
        # sleep(0.3)

        d = {0: {0: 0, 1: 1}, 1: {0: 1, 1: 0}, 2: {0: 0, 1: -1}, 3: {0: -1, 1: 0}}
        zx = xx * 2
        zy = yy * 2
        self.map1[zx][zy] = 1
        if randint(0, 1) == 1:
            turn = 1
        else:
            turn = 3
        next_value = randint(0, 3)
        for i in xrange(0, 4):
            if self.map1[zx + 2 * d[next_value][0]][zy + 2 * d[next_value][1]] == 0:
                self.map1[zx + d[next_value][0]][zy + d[next_value][1]] = 1
                self.search(xx + d[next_value][0], yy + d[next_value][1])
            next_value = (next_value + turn) % 4
        return 0

    def make_maze(self, xi, yi):
        z2 = 2 * yi + 2
        for z1 in xrange(0, 2 * xi + 2 + 1):
            self.map1[z1][0] = 1
            self.map1[z1][z2] = 1
        for z1 in xrange(0, 2 * yi + 2 + 1):
            self.map1[0][z1] = 1
            self.map1[z2][z1] = 1
        self.map1[1][2] = 1
        self.map1[2 * xi + 1][2 * yi] = 1
        self.end = (2 * xi + 1, 2 * yi)
        self.begin = (1, 2)
        self.search((randint(1, xi)), (randint(1, yi)))
        return

    def run(self):
        self.x = 22
        self.y = 22
        self.make_maze(self.x, self.y)
        self.render()

        self.find(self.begin[0], self.begin[1])
        self.render()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.render()
            # self.screen.blit(self.background, (0, 0))

            # for z2 in xrange(1, self.y * 2 + 1 + 1):
            #     for z1 in xrange(1, self.x * 2 + 1 + 1):
            #         if self.map1[z1][z2] == 0:
            #             self.screen.blit(self.diamonds1, (z1*10, z2*10))
            #         else:
            #             self.screen.blit(self.diamonds2, (z1*10, z2*10))
            #
            # pygame.display.update()

        return

    def render(self):

        self.screen.blit(self.background, (0, 0))

        for z2 in xrange(1, self.y * 2 + 1 + 1):
            for z1 in xrange(1, self.x * 2 + 1 + 1):

                if self.map1[z1][z2] == 0:
                    self.screen.blit(self.diamonds1, (z1*10, z2*10))
                elif self.map1[z1][z2] == 1:
                    self.screen.blit(self.diamonds2, (z1*10, z2*10))
                elif self.map1[z1][z2] == 2:
                    self.screen.blit(self.diamonds3, (z1*10, z2*10))
                # elif self.end[0] == z1 and self.end[1] == z2:
                #     self.screen.blit(self.red, (z1*10, z2*10))
                # elif self.begin[0] == z1 and self.begin[1] == z2:
                #     self.screen.blit(self.diamonds3, (z1*10, z2*10))
        self.screen.blit(self.yellow, (self.begin[0]*10, self.begin[1]*10))
        self.screen.blit(self.red, (self.end[0]*10, self.end[1]*10))

        pygame.display.update()

        return

    def find(self, x, y):
        self.render()
        index = self.index
        self.root[self.index] = (x, y)
        self.index += 1

        for i in xrange(0, 4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 < nx <= self.x * 2 + 1 and 0 < ny <= self.y * 2 + 1:
                if self.map1[nx][ny] == 1:
                    if nx == self.end[0] and ny == self.end[1]:
                        print self.index
                        return 1
                    self.map1[nx][ny] = 2
                    if 0 == self.find(nx, ny):
                        self.map1[nx][ny] = 1
                    else:
                        return 1

        self.index = index
        return 0

if __name__ == "__main__":
    app = App()
    app.run()
