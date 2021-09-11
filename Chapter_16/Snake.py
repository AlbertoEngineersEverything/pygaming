import pygame, sys, os
from pygame.locals import *
from mainWindow import Window

# Attempting to recreate a Snake clone

BLACK = (0, 0, 0)
window_width = 500
window_height = 500

pygame.init()
fps = 30
fpsClock = pygame.time.Clock()

main_surface = pygame.display.set_mode((window_width, window_height))

# Creating block
path_2_block_img = r"Assets_snake\wall.png"
block = pygame.image.load(path_2_block_img)
block_surface = block.get_rect()


# Creating Snake

# Creating berry


# game loop
while True:
    main_surface.fill(BLACK)

    main_surface.blit(block, block_surface)

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(fps)
