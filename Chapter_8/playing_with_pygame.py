#!C:\Users\Alberto\AppData\Local\Programs\Python\Python38\python

import pygame, os, sys
from pygame.locals import *

# initializing pygame
pygame.init()
# clamp the updated to 30 frames per second
fpsClock = pygame.time.Clock()
# set a surface to draw on or add spirits to.  This is set to 800x600 pixels
surface = pygame.display.set_mode((800, 600))

background = pygame.Color(100, 149, 237)  # the color represented by (100, 149, 237) is cornflower blue

# The main loop keeps the application refreshing and updating until the user quits
while True:
    surface.fill(background)  # This 'wipes' the window and resets it all to the background color

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # redraws the screen
    fpsClock.tick(30)  #