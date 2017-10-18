# Author: Robin Vogels

from OpenGL.GL import *
from OpenGL.GLU import *
from Logic import GameData
from Renderers import BlockRenderer

def render_world():
    BlockRenderer.renderBlock(0,0,0)
    BlockRenderer.renderBlock(2,0,0)
    BlockRenderer.renderBlock(-2,0,0)



