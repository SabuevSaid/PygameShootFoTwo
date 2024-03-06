import pygame
import config
pygame.init()
class Player:
    def __init__(self, w, h, keyList):
        self.w, self.h = w, h
        self.jump_size = 16
        self.graviti = True
        self.texture = pygame.image.load('items/mario2.png')
        self.subjects = config.subjects
        self.keyList = keyList
        self.is_jump = False
        self.on_earth = False
        self.graviti_size = 1
        self.up = keyList[0]
        self.right = keyList[1]
        self.left = keyList[2]
        self.rect = pygame.Rect(self.w, self.h, config.tile, config.tile)
        config.subjects.append(self)
    def update(self, keys):
        if keys[self.left]:
            if not any([pygame.Rect(self.w - 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.w -= 8
        elif keys[self.right]:
            if not any([pygame.Rect(self.w + 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.w += 8
        if self.on_earth:
            if keys[pygame.K_UP]:
                self.is_jump = True
                self.graviti_size = 1
        if self.is_jump:
            if self.jump_size > 0:
                self.graviti = False
            else:
                self.jump_size = 16
                self.graviti = True
                self.is_jump = False
            self.jump_size -= 1
        if not any([pygame.Rect(self.w, self.h + self.graviti_size, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
            self.on_earth = False
            if self.graviti:
                self.h += self.graviti_size
                self.graviti_size += 1
        else:
            self.on_earth = True
            self.is_jump = False
            self.graviti_size = 1
        if not self.graviti:
            self.h -= self.jump_size
    def draw(self):
        config.draw(self)
        config.output_on_display(f'wight: {self.w}, height: {self.h}')