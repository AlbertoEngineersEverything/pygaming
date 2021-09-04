#!C:\Users\Alberto\AppData\Local\Programs\Python\Python38\python

import pygame, os, sys
from pygame.locals import *

main_surface_height = 600
main_surface_width = 800

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((main_surface_width, main_surface_height))
pygame.display.set_caption('Bricks')

black = pygame.Color(0, 0, 0)

# bat init  # note: bat dims are 55x11
bat_path = r"Bricks/bat.png"
bat = pygame. image.load(bat_path)

# bat/player y-axis movement is restricted to 90% of total surface height
bat_y_restriction = 0.85 * main_surface_height

# instantiates the bat rectangle object
bat_rect = bat.get_rect()

# default mouse coordinates
mouse_x_axis, mouse_y_axis = (0, bat_y_restriction)

# ball init  # note: ball dims are 8x8
ball_path = r"Bricks/ball.png"
ball = pygame.image.load(ball_path)
ball_surface = ball.get_rect()

ball_starting_y_pos = 200
ball_speed = 3
ball_served = False

ball_x_position, ball_y_position = (24, ball_starting_y_pos)
ball_speed_x_axis, ball_speed_y_axis = (ball_speed, ball_speed)
ball_surface.topleft = (ball_x_position, ball_y_position)

# brick init  # note: brick dims are 31x16
brick_path = r"Bricks/brick.png"
brick = pygame.image.load(brick_path)
# creating a container to keep track of the brick objects
bricks = []

# creating the bricks
# creating the rows of bricks
for row in range(5):
    brick_rows_y_axis = (row * 24) + 100
    # creating the brick columns
    for col in range(10):
        brick_cols_x_axis = (col * 31) + 245
        brick_width = brick.get_width()
        brick_height = brick.get_height()
        brick_rect = Rect(brick_cols_x_axis,
                          brick_rows_y_axis,
                          brick_width,
                          brick_height)
        bricks.append(brick_rect)


while True:
    mainSurface.fill(black)
    # brick draw
    for each_brick in bricks:
        mainSurface.blit(brick, each_brick)

    # bat and ball draw
    mainSurface.blit(bat, bat_rect)  # adding the bat to the main surface
    mainSurface.blit(ball, ball_surface)   # adding the ball to the main surface

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:  # tracking the mouse input
            mouse_x_axis, mouse_y_axis = event.pos
            if mouse_x_axis < main_surface_width - 55:
                bat_rect.topleft = (mouse_x_axis, bat_y_restriction)
            else:
                bat_rect.topleft = (main_surface_width - 55, bat_y_restriction)
        elif event.type == MOUSEBUTTONUP and not ball_served:  # left click will launch ball
            ball_served = True

    # main game logic
        # Distance = Speed x Time
        # Time is fixed to 30 frames per second.
        # With ball_speed being 3, Distance(pixels) = 3(pixel/frame) x 30(frames/sec)
    if ball_served:
        ball_x_position += ball_speed_x_axis  # changing the x axis position by the speed
        ball_y_position += ball_speed_y_axis  # changing the y axis position by the speed

        # updating the position of the ball on the screen
        ball_surface.topleft = (ball_x_position, ball_y_position)

    # collision detection
    # adding a top boundary
    if ball_y_position <= 0:
        ball_y_position = 0
        ball_speed_y_axis *= -1

    # adding a left boundary
    if ball_x_position <= 0:
        ball_x_position = 0
        ball_speed_x_axis *= -1

    # adding a right boundary
    if ball_x_position >= main_surface_width - 8:
        ball_x_position = main_surface_width - 8
        ball_speed_x_axis *= -1

    # adding collision with bat
    if ball_surface.colliderect(bat_rect):
        ball_y_position = bat_y_restriction - 8
        ball_speed_y_axis *= -1

    # Commented out the bottom boundary because replacing
    # it with out of bounds
    # # adding bottom boundary
    # if ball_y_position >= main_surface_height - 8:
    #     ball_y_position = main_surface_height - 8
    #     ball_speed_y_axis *= -1

    # Adding out of bounds, where if the ball collides with the
    # bottom boundary will end the turn and reset the ball in its initial
    # coordinates.
    if ball_y_position >= main_surface_height - 8:
        ball_served = False
        ball_x_position, ball_y_position = 24, ball_starting_y_pos
        ball_speed = 3
        ball_speed_x_axis, ball_speed_y_axis = ball_speed, ball_speed_y_axis
        ball_surface.topleft = (ball_x_position, ball_y_position)

    # adding ball collision with brick detection
    # creating a count of bricks to collide with
    brick_hit_index = ball_surface.collidelist(bricks)
    if brick_hit_index >= 0:
        hb = bricks[brick_hit_index]
        ball_center_x_position = ball_x_position + 4
        ball_center_y_position = ball_y_position + 4

        if ball_center_x_position > hb.x + hb.width or ball_center_x_position < hb.x:
            ball_speed_x_axis *= -1
        else:
            ball_speed_y_axis *= -1

        del (bricks[brick_hit_index])

    pygame.display.update()
    fpsClock.tick(30)
