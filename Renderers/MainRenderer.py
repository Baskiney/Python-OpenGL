# Author: Robin Vogels

from Logic import GameData
from Logic import InputHandler
from Renderers import WorldRenderer
from Renderers import HUDRenderer

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


def init():
        pygame.init()
        pygame.display.set_caption(GameData.titleName)
        pygame.display.set_icon(pygame.image.load('eufh.jpg'))
        GameData.window = pygame.display.set_mode(GameData.resolution, pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.font.init()
        print("Renderer Initiated!")
        glClearColor(0.5, 0.7, 1.0, 1.0)
        gluPerspective(GameData.fieldOfView, (GameData.resolution[0] / GameData.resolution[1]), 0.5, 100.0)


def render_loop():
    while True:
        InputHandler.handle_input()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        WorldRenderer.render_world()
        #HUDRenderer.render_hud()


        pygame.display.flip()
        GameData.clock.tick(GameData.targetFPS)
        pygame.display.set_caption(GameData.titleName + "  FPS: "+(str(round(GameData.clock.get_fps(),1))))



