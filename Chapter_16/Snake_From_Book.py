#!/usr/bin/python3
import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameData(object):
    def __init__(self):
        self.lives = 3          # Lives: number of attempts
        self.isDead = False     # isDead: set true when snake's head touches snake or wall
        self.blocks = []        # blocks: The list of blocks that make up snake body
        self.tick = 250         # tick: The running total used to count down to the next animation frame. In milliseconds
        self.level = 1          # level: Current level of difficulty
        self.berryCount = 0     # berrycount: Number of berries consumed by the snake in current level
        self.segments = 1       # segments: The number of segments added when berry is consumed
        self.frame = 0          # Current animation frame used to draw snake's head(snake has 2 frames of animation)
        self.speed = 250        # speed: The default tick speed, in milliseconds

        # Generating the random position coordinates of a berry
        bx = random.randint(1, 38)
        by = random.randint(1, 28)
        self.berry = Position(bx, by)

        self.blocks.append(Position(20, 15))
        self.blocks.append(Position(19, 15))
        self.direction = 0


def lose_life(gamedata):
    # gamedata.lives -= 1
    pass


def position_berry(gamedata):
    pass


def load_map_file(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    return content


def head_hits_body(gamedata):
    return False


def head_hits_wall(map, gamedata):
    return False


def draw_data(surface, gamedata):
    pass


def draw_game_over(surface):
    text1 = font.render("GAME OVER", True, (255, 255, 255))
    text2 = font.render("SPACE BAR to play OR close the window to QUIT", True, (255, 255, 255))
    #  The .render method creates a PyGame surface that will fit the text exactly
    #  The parameters for the .render(<String to display>, <anti-alaising>, <color>)
    cx = surface.get_width() / 2
    cy = surface.get_height() / 2
    textpos1 = text1.get_rect(centerx=cx, top=cy - 48)
    textpos2 = text2.get_rect(centerx=cx, top=cy)

    surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)


def draw_walls(surface, img, map):
    pass


def draw_snake(surface, img, gamedata):
    pass


def update_game(gamedata, gametime):
    pass


def load_images():
    wall = pygame.image.load(r'Assets_snake\wall.png')
    raspberry = pygame.image.load(r'Assets_snake\berry.png')
    snake = pygame.image.load(r'Assets_snake\snake.png')

    return {'wall': wall, 'berry': raspberry, 'snake': snake}


images = load_images()
images['berry'].set_colorkey((255, 0, 255))

snakemap = load_map_file(r'Assets_snake\map.txt')
data = GameData()
quitGame = False
isPlaying = False

while not quitGame:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if isPlaying:
        x = random.randint(1, 38)
        y = random.randint(1, 38)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16      # X coord mult. by 16 because each cell 16x16
        rrect.top = data.berry.y * 16       # Y coord mult. by 16 because each cell 16x16

    # Do update stuff here

        isPlaying = (data.lives > 0)        # Confirms that if there are lives left, playing continues
                                            # This changes the original False value for isPlaying
        if isPlaying:
            surface.fill((0, 0, 0))

            # Do drawing stuff here
            draw_walls(surface, images['wall'], snakemap)
            surface.blit(images['berry'], rrect)
            draw_snake(surface, images['snake'], data)
            draw_data(surface, data)

    else:
        # Add the message that the game is over
        # Give the player the options to press the 'space bar' to play again
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            isPlaying = True            # Resets isPlaying to True so the came can continue
            data = None                 # Deletes the data object
            data = GameData()           # Recreates the GameData default values

        draw_game_over(surface)

    pygame.display.update()
    fpsClock.tick(30)