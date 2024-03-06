import pygame
import config
pygame.init()
class Block:
    def __init__(self, h, w, texture_type):
        self.type = 'block'
        self.texture_type = texture_type
        self.texture = pygame.image.load(f'items/{texture_type}.png')
        self.w, self.h = w, h
        self.rect = pygame.Rect(self.w, self.h, config.tile, config.tile)
        config.objects.append(self)
    def update(self):
        pass
    def draw(self):
        config.draw(self)