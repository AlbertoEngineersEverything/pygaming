import pygame, os, sys
from pygame.locals import *

class Bat:
    def __init__(self, x=0, y=700, path_to_bat_image='Asset_bat/bat.png'):
        self.x_position = x
        self.y_restricted_position = y
        self.bat_image = pygame.image.load(path_to_bat_image)

