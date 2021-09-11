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
    pass


def position_berry(gamedata):
    pass


def load_map_file(file_name):
    return None


def head_hits_body(gamedata):
    return False


def head_hits_wall(map, gamedata):
    return False


def draw_data(surface, gamedata):
    pass


def draw_game_over(surface):
    pass


def draw_walls(surface, img, map):
    pass


def draw_snake(surface, img, gamedata):
    pass


def update_game(gamedata, gametime):
    pass


def load_images():
    return {}


