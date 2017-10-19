# Author: Robin Vogels

from OpenGL.GL import *
from OpenGL.GLU import *
from Logic import GameData
from Renderers import BlockRenderer

def render_world():
    BlockRenderer.renderBlock(0,2,0)
    BlockRenderer.renderBlock(2,0,0)
    BlockRenderer.renderBlock(-2,0,0)
    BlockRenderer.renderBlock(4,-2,0)
    BlockRenderer.renderBlock(8,2,0)
    BlockRenderer.renderBlock(10,0,0)
    BlockRenderer.renderBlock(6,0,0)
    BlockRenderer.renderBlock(-4,-2,0)
    BlockRenderer.renderBlock(-4,-4,0)
    BlockRenderer.renderBlock(-2,-6,0)
    BlockRenderer.renderBlock(0,-8,0)
    BlockRenderer.renderBlock(2,-10,0)
    BlockRenderer.renderBlock(4,-12,0)
    BlockRenderer.renderBlock(6,-10,0)
    BlockRenderer.renderBlock(8,-8,0)
    BlockRenderer.renderBlock(10,-6,0)
    BlockRenderer.renderBlock(12,-4,0)
    BlockRenderer.renderBlock(12,-2,0)
    BlockRenderer.renderBlock(10,0,0)


