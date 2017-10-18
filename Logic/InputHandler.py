# Author: Robin Vogels

import pygame
from Renderers import Camera

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                Camera.move_forward()
            elif event.button == 5:
                Camera.move_backward()

