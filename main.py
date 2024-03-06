import pygame
from player import *
import maps
from block import *
from config import *
import shot
pygame.init()
for h in range(20):
    for w in range(40):
        if maps.maps[0][h][w] == '#':
            Block(h * tile, w * tile, 'zemla')
        if maps.maps[0][h][w] == '+':
            Block(h * tile, w * tile, 'trava')
player = Player(player_x, player_y, (pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT))
while play:
    keys = pygame.key.get_pressed()
    pygame.display.update()
    window.blit(bg, (0, 0))
    for obj in objects:
        obj.update()
    for obj in objects:
        obj.draw()
    for sub in subjects:
        sub.update(keys)
    for sub in subjects:
        sub.draw()
    for sh in shots:
        sh.update()
    for sh in shots:
        sh.draw()
    fps.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()