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
        self.rect = pygame.Rect(self.w, self.h, config.tile, config.tile)
        config.subjects.append(self)
    def update(self, keys):
        self.anim = 0
        if keys[self.left]:
            if not any([pygame.Rect(self.w - 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.w -= 5
                self.direct = 'left'
                if self.anim >= 3:
                    self.anim = 0
                else:
                    self.anim += 1
        elif keys[self.right]:
            if not any([pygame.Rect(self.w + 7, self.h, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.w += 5
                self.direct = 'right'
                if self.anim >= 3:
                    self.anim = 0
                else:
                    self.anim += 1
        if self.on_earth:
            if keys[pygame.K_UP] and not keys[pygame.K_SPACE]:
                self.is_jump = True
                self.graviti_size = 1
        if self.is_jump:
            if self.direct == 'right':
                self.anim = 0
                self.direct = 'up'
            else:
                self.anim = 1
                self.direct = 'up'
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
            if not any([pygame.Rect(self.w, self.h - self.jump_size, config.tile, config.tile).colliderect(obj.rect) for obj in config.objects]):
                self.h -= self.jump_size
        if keys[pygame.K_SPACE]:
            if self.direct == 'right':
                shot.Shot(self.w + config.tile - 6, self.h + 24, self.direct)
            elif self.direct == 'left':
                shot.Shot(self.w - 6, self.h + 24, self.direct)
            elif self.direct == 'up':
                if self.anim == 1:
                    shot.Shot(self.w - 6, self.h + 24, 'left')
                elif self.anim == 0:
                    shot.Shot(self.w + config.tile - 6, self.h + 24, 'right')
            elif self.direct == 'down':
                if keys[pygame.K_DOWN]:
                    shot.Shot(self.w + config.tile / 2, self.h + config.tile, 'down')
        if keys[pygame.K_DOWN]:
            if self.direct == 'left':
                self.anim = 1
            elif self.direct == 'right':
                self.anim = 0
            elif self.direct == 'up':
                self.anim = 0
            self.direct = 'down'
        elif keys[pygame.K_KP0]:
            shot.Shot(self.w + config.tile / 2, self.h, 'up')
    def draw(self):
        self.texture = config.turns[self.direct][self.anim]
        config.draw(self)
        config.output_on_display(f'wight: {self.w}, height: {self.h}')