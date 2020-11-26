import sys
import pygame
from pygame.locals import *

pygame.init()


KEYS_DOWN = []


class SCREEN:
    _WIDTH = 800
    _HEIGHT = 600
    _SIZE = [_WIDTH, _HEIGHT]


Screen = pygame.display.set_mode(SCREEN._SIZE)

CLOCK = pygame.time.Clock()
FPS = 60

BG_COLOUR = [50, 205, 50]
IS_RUNNING = True


class P1:
    _Lives = 5
    _points = 100
    _sprite = pygame.image.load("../Art/spr_Player.png")
    _Rect = _sprite.get_rect()
    _speed = 5
    
    def method(self):
        print(f"Lives: {P1._Lives}")


while IS_RUNNING:

    KEYS_DOWN = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False
    
    if (KEYS_DOWN[K_UP]):
        P1._Rect.y -= P1._speed
    elif (KEYS_DOWN[K_DOWN]):
        P1._Rect.y += P1._speed

    if (KEYS_DOWN[K_LEFT]):
        P1._Rect.x -= P1._speed
    elif (KEYS_DOWN[K_RIGHT]):
        P1._Rect.x += P1._speed
   
    Screen.fill(BG_COLOUR)
   
    Screen.blit(P1._sprite, P1._Rect)
   
    pygame.display.flip()
   
    CLOCK.tick(FPS)

