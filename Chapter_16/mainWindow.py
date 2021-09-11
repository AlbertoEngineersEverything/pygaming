import pygame
## Not ready yet

class Window():
    width = 500
    height = 500
    BLACK = pygame.Color(0, 0, 0)  # default background is black
    background_color = None
    title_caption = ""

    def __init__(self, w=500 , h=500, background_color=(100,100,100), game="Don't Forget To Name ME!"):
        self.width = w
        self.height = h
        self.title_caption = game
        if len(background_color) == 3:
            self.background_color = pygame.Color(background_color)
        else:
            self.background_color = self.BLACK

    def create_main_surface(self):
        return pygame.display.set_mode((self.width, self.height))