import pygame

pygame.init()
fps = pygame.time.Clock()
tile = 48
pygame.display.set_caption('mario')
icon = pygame.image.load('items/icon.png')
pygame.display.set_icon(icon)
rect = pygame.Surface((tile * 2, tile * 2))
rect.fill('Red')
text = pygame.font.Font('items/text.ttf', 48)
def draw(obj):
     window.blit(obj.texture, (obj.w, obj.h))
def output_on_display(s):
     window.blit(text.render(f'{s}', False, (255, 255, 255)), (100, tile * 18))
window = pygame.display.set_mode((tile * 40, tile * 20))
bg = pygame.image.load('items/nebo.png')
turns = {'left': [
     pygame.image.load('items/mario_left2.png'),
     pygame.image.load('items/mario_left3.png'),
     pygame.image.load('items/mario_left4.png'),
     pygame.image.load('items/mario_left5.png'),
], 'right': [
     pygame.image.load('items/mario_right2.png'),
     pygame.image.load('items/mario_right3.png'),
     pygame.image.load('items/mario_right4.png'),
     pygame.image.load('items/mario_right5.png'),
], 'jump': [
     pygame.image.load('items/mario_right_jump.png'),
     pygame.image.load('items/mario_left_jump.png')
], 'down': [
     pygame.image.load('items/mario_right2.png'),
     pygame.image.load('items/mario_left2.png'),
], 'up': [
     pygame.image.load('items/mario_right2.png'),
     pygame.image.load('items/mario_left2.png')
]}
play = True
player_x = tile * 20
player_y = tile * 10
objects = []
subjects = []
shots = []