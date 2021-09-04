#!C:\Users\Alberto\AppData\Local\Programs\Python\Python38\python

import pygame, os, sys
from pygame.locals import *

# initializing pygame
pygame.init()
# starts the clock, with an aim of 30 frames/sec
fpsClock = pygame.time.Clock()
# set a surface to draw on or add spirits to.  This is set to 800x600 pixels
surface = pygame.display.set_mode((800, 600))

background = pygame.Color(100, 149, 237)  # the color represented by (100, 149, 237) is cornflower blue

# The main loop keeps the application refreshing and updating until the user quits
while True:
    surface.fill(background)  # This 'wipes' the window and resets it all to the background color

    # loading and image is pretty simple:
    path2image = r"D:\CodingProjects\pygamebook\Chapter_9\Assets\toycar.png"
    image = pygame.image.load(path2image)

    # Draw the image to a surface
    surface.blit(image, (0, 0))  # the image would be added to the top-left of the window
    # surface.blit(image, (0, 0), (32, 0, 32, 32))  # The second tuple, is (x, y, width, height) of the sprite sheet

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # redraws the screen
    fpsClock.tick(30)  # clamp the updated to 30 frames per second


