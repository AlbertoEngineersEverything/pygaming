import pygame
from robotmodel import RobotModel


class RadarView(object):
    def __init__(self, blipImagePath, borderImagePath):
        self.blip_image = pygame.image.load(blipImagePath)
        self.border_image = pygame.image.load(borderImagePath)

    def draw(self, surface, robots):
        for robot in robots:
            x, y = robot.get_position()
            x /= 10
            y /= 10

            x += 1
            y += 1

            surface.blit(self.blip_image, (x, y))

        surface.blit(self.border_image, (0, 0))
        