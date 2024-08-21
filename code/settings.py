import pygame
from os.path import join

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BG = pygame.image.load(join('assets','board','Board.png'))
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60