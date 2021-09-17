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
        self.tick = 250         # tick: Total used to count down to the next animation frame. In milliseconds
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
    gamedata.lives -= 1         # subtraction of 1 life
    gamedata.direction = 0      # resets the direction fo the snake
    gamedata.blocks[:] = []     # when the player loses a life, the length of the snake is reset

    gamedata.blocks.append(Position(20, 15))    # adds 2 blocks to the snake's body
    gamedata.blocks.append(Position(19, 15))


def position_berry(gamedata):
    bx = random.randint(1, 38)
    by = random.randint(1, 28)
    found = True

    while found:
        found = False
        for b in gamedata.blocks:
            if b.x == bx and b.y == by:
                found = True
        if found:
            bx = random.randint(1, 38)
            by = random.randint(1, 28)

    gamedata.berry = Position(bx, by)


def load_map_file(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    return content


def head_hits_body(gamedata):
    head = gamedata.blocks[0]
    for b in gamedata.blocks:
        if b != head:
            if b.x == head.x and b.y == head.y:
                return True
        return False


def head_hits_wall(map, gamedata):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if char == '1':
                if gamedata.blocks[0].x == col and gamedata.blocks[0].y == row:
                    return True
            col += 1
        row += 1
    return False


def draw_data(surface, gamedata):
    text = "Lives = {0}, Level = {1}"
    info = text.format(gamedata.lives, gamedata.level)
    text = font.render(info, 0, (255, 255, 255))
    textpos = text.get_rect(centerx=surface.get_width() / 2, top=32)
    surface.blit(text, textpos)


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
    row = 0
    for line in map:
        col = 0
        for char in line:
            if char == '1':
                imgRect = img.get_rect()
                imgRect.left = col * 16
                imgRect.top = row * 16
                surface.blit(img, imgRect)
            col += 1
        row += 1


def draw_snake(surface, img, gamedata):
    first = True    # First is referancing the head of the snake
    right = 0       # Directions are associated with the numbers
    left = 1        # as the number will be multiplied by 16, will
    up = 2          # specify the section of the sprite sheet.
    down = 3
    for b in gamedata.blocks:
        dest = (b.x * 16, b.y * 16, 16, 16)

        if first:
            first = False
            src = (((gamedata.direction * 2) + gamedata.frame) * 16, 0, 16, 16)
        else:
            src = (8 * 16, 0, 16, 16)

        surface.blit(img, dest, src)


def update_game(gamedata, gametime):
    gamedata.tick -= gametime
    head = gamedata.blocks[0]

    if gamedata.tick < 0:
        gamedata.tick += gamedata.speed
        gamedata.frame += 1
        gamedata.frame %= 2

        if gamedata.direction == 0:
            move = (1, 0)
        elif gamedata.direction == 1:
            move = (-1, 0)
        elif gamedata.direction == 2:
            move = (0, -1)
        else:
            move = (0, 1)

        newpos = Position(head.x + move[0], head.y + move[1])

        first = True
        for b in gamedata.blocks:
            temp = Position(b.x, b.y)
            b.x = newpos.x
            b.y = newpos.y
            newpos = Position(temp.x, temp.y)

    keys = pygame.key.get_pressed()

    if keys[K_RIGHT] and gamedata.direction != 1:
        gamedata.direction = 0
    elif keys[K_LEFT] and gamedata.direction != 0:
        gamedata.direction = 1
    elif keys[K_UP] and gamedata.direction != 3:
        gamedata.direction = 2
    elif keys[K_DOWN] and gamedata.direction != 2:
        gamedata.direction = 3

    if head.x == gamedata.berry.x and head.y == gamedata.berry.y:
        lastIdx = len(gamedata.blocks) - 1
        for index in range(gamedata.segments):
            blockX = gamedata.blocks[lastIdx].x
            blockY = gamedata.blocks[lastIdx].y
            gamedata.blocks.append(Position(blockX, blockY))

            bx = random.randint(1, 38)
            by = random.randint(1, 28)
            gamedata.berry = Position(bx, by)
            gamedata.berryCount += 1

            if gamedata.berryCount == 10:
                gamedata.berryCount = 0
                gamedata.speed -= 25
                gamedata.level += 1
                gamedata.segments *= 2
                if gamedata.segments > 64:
                    gamedata.segments = 64

                if gamedata.speed < 100:
                    gamedata.speed = 100


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
        update_game(data, fpsClock.get_time())

        crashed = head_hits_wall(snakemap, data) or head_hits_body(data)

        if crashed:
            lose_life(data)
            position_berry(data)

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