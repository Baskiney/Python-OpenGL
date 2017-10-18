# Author: Robin Vogels

import pygame

# All relevant Game Data
# Strings
titleName = "Python OpenGL Test"
playerName = "Robin"

# Numerics
resolution = (1024,768)
fieldOfView = 90
targetFPS = 30
playerSpeed = 0.5
playerPosX = 0
playerPosY = 0
playerPosZ = -5

# Booleans
paused = False


# Set advanced Models ...
clock = pygame.time.Clock()
window = None
