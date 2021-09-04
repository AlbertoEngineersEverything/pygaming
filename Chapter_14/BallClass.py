
import pygame, os, sys
from pygame.locals import *

# creating the Ball class


class Ball:

    def __init__(self, x, y, speed, path_to_image):
        self.x_position = x
        self.y_position = y
        self.ball_speed = speed
        self.ball_image = pygame.image.load(path_to_image)

    def update(self, game_time):
        ball_speed_on_x_axis = self.ball_speed[0]
        ball_speed_on_y_axis = self.ball_speed[1]

        self.x_position += ball_speed_on_x_axis
        self.y_position += ball_speed_on_y_axis

        if self.y_position <= 0:
            self.y_position = 0
            ball_speed_on_y_axis *= -1

        if self.y_position >= 600 - 8:
            self.y_position = 600 - 8
            ball_speed_on_y_axis *= -1

        if self.x_position <= 0:
            self.x_position = 0
            ball_speed_on_x_axis *= -1

        if self.x_position >= 800 - 8:
            self.x_position = 800 - 8
            ball_speed_on_x_axis *= -1

        self.ball_speed = (ball_speed_on_x_axis, ball_speed_on_y_axis)

    def has_hit_brick(self, bricks):
        return False

    def has_hit_bat(self, bat):
        return False

    def draw(self, game_time, surface):
        surface.blit(self.ball_image, (self.x_position, self.y_position))


if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))

    ball = Ball(0, 200, (4, 4), 'Asset_ball/ball.png')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ball.update(fpsClock)
        surface.fill((0, 0, 0))
        ball.draw(fpsClock, surface)

        pygame.display.update()
        fpsClock.tick(30)

