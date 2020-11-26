import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
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


class Player:
    _Sprite = pygame.image.load("../Art/spr_Player.png")
    _Rect = _Sprite.get_rect()
    _Speed = 5


while IS_RUNNING:

    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()

    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False

    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    if (KEYS_DOWN[K_UP]):
        Player._Rect.y -= Player._Speed
    elif (KEYS_DOWN[K_DOWN]):
        Player._Rect.y += Player._Speed

    if (KEYS_DOWN[K_LEFT]):
        Player._Rect.x -= Player._Speed
    elif (KEYS_DOWN[K_RIGHT]):
        Player._Rect.x += Player._Speed

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    Screen.fill(BG_COLOUR)

    # Then draw sprites on the current location:
    Screen.blit(Player._Sprite, Player._Rect)

    # Finally refresh the entire screen of this application window:
    pygame.display.flip()

    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
