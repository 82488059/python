# -*- coding:utf-8 -*-
from random import randint

import pygame
from pygame.locals import *


MAZE_MAX = 50

map1 = {}
for x in xrange(0, MAZE_MAX + 2):
    map1[x] = {}
    for y in xrange(0, MAZE_MAX + 2):
        map1[x][y] = 0


def search(xx, yy):
    d = {0: {0: 0, 1: 1}, 1: {0: 1, 1: 0}, 2: {0: 0, 1: -1}, 3: {0: -1, 1: 0}}
    zx = xx * 2
    zy = yy * 2
    map1[zx][zy] = 1
    if randint(0, 1) == 1:
        turn = 1
    else:
        turn = 3
    next_value = randint(0, 3)
    for i in xrange(0, 4):
        if map1[zx + 2 * d[next_value][0]][zy + 2 * d[next_value][1]] == 0:
            map1[zx + d[next_value][0]][zy + d[next_value][1]] = 1
            search(xx + d[next_value][0], yy + d[next_value][1])
        next_value = (next_value + turn) % 4
    return 0


def make_maze(xi, yi):
    z2 = 2 * yi + 2
    for z1 in xrange(0, 2 * xi + 2 + 1):
        map1[z1][0] = 1
        map1[z1][z2] = 1
    for z1 in xrange(0, 2 * yi + 2 + 1):
        map1[0][z1] = 1
        map1[z2][z1] = 1
    map1[1][2] = 1
    map1[2 * xi + 1][2 * yi] = 1
    search((randint(1, xi)), (randint(1, yi)))
    return


def run():
    x = 22
    y = 22
    make_maze(x, y)
    # for z2 in xrange(1, y * 2 + 1 + 1):
    #     str1 = ""
    #     for z1 in xrange(1, x * 2 + 1 + 1):
    #         if map1[z1][z2] == 0:
    #             str1 += "-"  # print "█"
    #         else:
    #             str1 += " "  # print " "
    #     if z2 <= y * 2:
    #         print str1 + "\n"

    screen_size = (640, 480)
    diamonds_size = (10, 10)
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    background = pygame.surface.Surface(screen_size).convert()
    diamonds1 = pygame.surface.Surface(diamonds_size).convert()
    diamonds2 = pygame.surface.Surface(diamonds_size).convert()
    background.fill((255, 255, 255))
    diamonds1.fill((128, 128, 128))
    diamonds2.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))

        for z2 in xrange(1, y * 2 + 1 + 1):
            for z1 in xrange(1, x * 2 + 1 + 1):
                if map1[z1][z2] == 0:
                    screen.blit(diamonds1, (z1*10, z2*10))
                else:
                    screen.blit(diamonds2, (z1*10, z2*10))

        pygame.display.update()

    return 0


if __name__ == "__main__":
    run()
