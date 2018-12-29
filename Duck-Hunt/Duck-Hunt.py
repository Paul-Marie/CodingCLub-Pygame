#/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from random import randint

pygame.init()

background = pygame.image.load("Image/Background.png")
duck = pygame.image.load("Image/Duck-Sprite.png")
surface = [(0, 0, 110, 110), (110, 0, 110, 110), (220, 0, 110, 110)]
size_x = 1280
size_y = 769
position_x = 0
position_y = 0
milliseconds = 0
clock = pygame.time.Clock()
leave = False

window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Mon super jeu video")

state = 0
while not leave:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(pygame.mouse.get_pressed())
        if (mouse_x >= position_x and mouse_x <= position_x + 110 and mouse_y >= position_y
        and mouse_y <= position_y + 110) and pygame.mouse.get_pressed()[0] is 1:
            position_x = 0
            position_y = randint(0, size_y - 110)
        print(event)
    clock.tick()
    milliseconds = milliseconds + clock.get_time()
    position_x = position_x + 1
    if position_x >= size_x:
        position_x = -300
    if milliseconds >= 100:
        state = (state + 1) % 3
        milliseconds = 0
    window.blit(background, (0, 0))
    window.blit(duck, (position_x, position_y), surface[state])
    pygame.display.update()

pygame.quit()
quit()
