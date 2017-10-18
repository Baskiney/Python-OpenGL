# Author: Robin Vogels

from OpenGL.GL import *
from Logic import GameData


def move_forward():
    glTranslatef(0, 0, GameData.playerSpeed)


def move_backward():
    glTranslatef(0, 0, -GameData.playerSpeed)


def move_right():
    glTranslatef(-GameData.playerSpeed, 0, 0)


def move_left():
    glTranslatef(+GameData.playerSpeed, 0, 0)


