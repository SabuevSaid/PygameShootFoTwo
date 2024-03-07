import time

import pygame
import config
import shot
pygame.init()
class Player:
    def __init__(self, w, h, keyList):
        self.w, self.h = w, h
        self.direct = 'right'
        self.jump_size = 16
        self.graviti = True
        self.anim = 0
        self.subjects = config.subjects
        self.keyList = keyList
        self.is_jump = False
        self.on_earth = False
        self.texture = [0, 0]
        self.graviti_size = 1
        self.up = keyList[0]
        self.right = keyList[1]
        self.left = keyList[2]
        self.down = keyList[3]
        self.jump = keyList[4]
        self.shoot = keyList[5]
        self.rect = pygame.Rect(self.w, self.h, config.tile, config.tile)
        config.subjects.append(self)
    def upn(self):
        if self.direct == 'right':
            self.anim = 0
            self.direct = 'up'
        else:
            self.anim = 1
            self.direct = 'up'
    def jumpn(self):
        if self.on_earth:
            self.is_jump = True
            self.graviti_size = 1
        if self.is_jump:
            self.direct = 'jump'
            if self.jump_size > 0:
                self.graviti = False
            else:
                self.jump_size = 16
                self.graviti = True
                self.is_jump = False
            self.jump_size -= 1
    def gravitin(self):
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
            if not any([pygame.Rect(self.w, self.h - self.jump_size, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.h -= self.jump_size
    def leftn(self):
        if not any([pygame.Rect(self.w - 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
            self.w -= 5
            self.direct = 'left'
            if self.anim >= 3:
                self.anim = 0
            else:
                self.anim += 1
    def rightn(self):
        if not any([pygame.Rect(self.w + 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
            self.w += 5
            self.direct = 'right'
            if self.anim >= 3:
                self.anim = 0
            else:
                self.anim += 1
    def downn(self):
        if self.direct == 'left':
            self.anim = 1
        elif self.direct == 'right':
            self.anim = 0
        elif self.direct == 'up':
            self.anim = 0
        self.direct = 'down'
    def shotn(self):
            if self.direct == 'right':
                shot.Shot(self.w + config.tile - 6, self.h + 24, self.direct)
            elif self.direct == 'left':
                shot.Shot(self.w - 6, self.h + 24, self.direct)
            elif self.direct == 'up':
                shot.Shot(self.w + config.tile / 2, self.h, 'up')
            elif self.direct == 'down':
                shot.Shot(self.w + config.tile / 2, self.h + config.tile, 'down')
    def update(self, keys):
        self.anim = 0
        if keys[self.left]:
            self.leftn()
        elif keys[self.right]:
            self.rightn()
        elif keys[self.down]:
            self.downn()
        elif keys[self.up]:
            self.upn()
        elif keys[self.jump]:
            self.jumpn()
        if keys[self.shoot]:
            self.shotn()
        self.gravitin()
    def draw(self):
        self.texture = config.turns[self.direct][self.anim]
        config.draw(self)
        config.output_on_display(f'wight: {self.w}, height: {self.h}')