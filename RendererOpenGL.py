import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

face = Model('model.obj', 'model.bmp')
face.position.z = -5

rend.scene.append( face )

isRunning = True
while isRunning:


    
    rend.render()

    pygame.display.flip()

pygame.quit()
