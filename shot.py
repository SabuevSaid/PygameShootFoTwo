import pygame
from config import *
pygame.init()
class Shot:
    def __init__(self, w, h, direct):
        self.type = 'shot'
        self.w, self.h = w, h
        self.direct = direct
        self.rect = pygame.Rect(self.w, self.h, 5, 5)
        shots.append(self)
    def update(self):
        self.rect = pygame.Rect(self.w, self.h, 5, 5)
        if self.direct == 'right':
            self.w += 10
        elif self.direct == 'left':
            self.w -= 10
        elif self.direct == 'up':
            self.h -= 10
        elif self.direct == 'down':
            self.h += 10
        if self.w >= tile * 40:
            shots.remove(self)
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                objects.remove(obj)
                if self in shots:
                  shots.remove(self)
    def draw(self):
        pygame.draw.circle(window, 'Red', (self.w, self.h), 2)