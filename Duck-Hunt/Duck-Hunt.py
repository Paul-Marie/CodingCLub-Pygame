#/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mon super jeu video")
clock = pygame.time.Clock()
leave = False

while not leave:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
