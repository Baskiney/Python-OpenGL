# Author: Robin Vogels

from Renderers import MainRenderer
from Logic import GameData


if __name__ == "__main__":
    print("Start successful!")

    MainRenderer.init()
    MainRenderer.render_loop()


    #TODO
    #GLEW/GLUT für Kamera Berechnung
    #Umstellung auf MVP Projektionsmatrix OpenGL4.1+




