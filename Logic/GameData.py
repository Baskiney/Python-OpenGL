# Author: Robin Vogels

import pygame

# All relevant Game Data
# Strings
titleName = "Python OpenGL Test"
playerName = "Robin"

# Numerics
resolution = (800,600)
fieldOfView = 90
targetFPS = 60
playerSpeed = 0.5
playerPosX = 0
playerPosY = 0
playerPosZ = -5
mousePosX = 0
mousePosY = 0

# Booleans
paused = False


# Set advanced Models ...
clock = pygame.time.Clock()
window = None
