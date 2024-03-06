import pygame
import config
pygame.init()
class Shot:
    def __init__(self, x, y):
        self.type = 'shot'
        self.x, self.y = x, y
        self.rect = pygame.Rect(self.x, self.y, config.tile, config.tile)
        config.objects.append(self)
    def shot(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass