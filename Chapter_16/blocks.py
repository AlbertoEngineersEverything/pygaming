import pygame, sys


class Block:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

        self.path = r"Assets_snake\wall.png"
        self.height = 16
        self.width = 16
        self.image = pygame.image.load(self.path)


class BlockBorder(object):
    def __init__(self, win):
        self.border_width = win.get_width()
        self.border_height = win.get_height()
        self.top_n_bottom = []
        self.left_n_right = []
        x = 0
        y = 0
        # building top and bottom boarders
        for each in range(int(self.border_width/16)):
            x_block = Block(x, y)
            self.top_n_bottom.append(x_block)
            x += 16
            if x >= self.border_width:
                x = 0
                y = self.border_height - 16
        y = 16
        for each in range(int(self.border_height/16)):
            y_block = Block(x, y)
            self.left_n_right.append(y_block)
            y += 16
            if y >= self.border_height - 16:
                y = 16
                x = self.border_width - 16

    def get_border_sequences(self):
        return self.top_n_bottom + self.left_n_right



pygame.init()
window = pygame.display.set_mode((500,500))
fpsClock = pygame.time.Clock()

while True:
    window.fill((0, 0, 0))
    border = BlockBorder(window)
    border_seq = border.get_border_sequences()
    for each in border_seq:
        window.blit(each)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(30)
