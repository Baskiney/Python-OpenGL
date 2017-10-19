# Author: Robin Vogels

import pygame
from Renderers import Camera
from Logic import GameData

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_w:
                Camera.move_forward()
            elif event.key == pygame.K_a:
                Camera.move_left()
            elif event.key == pygame.K_s:
                Camera.move_backward()
            elif event.key == pygame.K_d:
                Camera.move_right()
            elif event.key == pygame.K_SPACE:
                Camera.move_up()
            elif event.key == pygame.K_LSHIFT:
                Camera.move_down()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                Camera.move_forward()
            elif event.button == 5:
                Camera.move_backward()
        if event.type == pygame.MOUSEMOTION:
            (GameData.mousePosX,GameData.mousePosY) = event.pos


