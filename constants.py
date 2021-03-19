import pygame
import random

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
ICON = pygame.image.load('background/icon.jpg')

USR_WIDTH = 100
USR_HEIGHT = 80
USR_X = DISPLAY_WIDTH // 3

BARRIER_IMG = [pygame.image.load('barriers/barr0.png'), pygame.image.load('barriers/barr1.png'),
               pygame.image.load('barriers/barr2.png')]
BARRIER_OPTIONS = [70, 473, 40, 468, 30, 448]  # ширина и высота относительно дисплея для каждого барьера

CLOCK = pygame.time.Clock()
