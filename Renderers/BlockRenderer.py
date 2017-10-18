# Author: Robin Vogels

from OpenGL.GL import *
from OpenGL.GLU import *

# Geometry
# Cube
cubeVertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)
cubeEdges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def renderBlock(x,y,z):
    glTranslate(x,y,z)
    glBegin(GL_LINES)
    for edge in cubeEdges:
        for vertex in edge:
            glVertex3fv(cubeVertices[vertex])
    glEnd()
    glTranslate(-x, -y, -z)