import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
ICON = pygame.image.load('assets/background/icon.jpg')

USR_WIDTH = 90
USR_HEIGHT = 80
USR_X = DISPLAY_WIDTH // 3
PRIME_USR_Y = DISPLAY_HEIGHT - USR_HEIGHT - 82

BARRIER_IMG = [pygame.image.load('assets/barriers/barr0.png'), pygame.image.load('assets/barriers/barr1.png'),
               pygame.image.load('assets/barriers/barr2.png')]
BARRIER_OPTIONS = [[70, 473],
                   [40, 468],
                   [30, 448]]  # ширина и высота относительно дисплея для каждого барьера

WIZARD_IMG = [pygame.image.load('assets/character/wizard0.png'), pygame.image.load('assets/character/wizard1.png'),
               pygame.image.load('assets/character/wizard2.png'), pygame.image.load('assets/character/wizard3.png')]

CLOCK = pygame.time.Clock()
