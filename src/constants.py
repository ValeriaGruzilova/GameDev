import os
import sys
import pygame


def resource_path(relative):
    """Function to find and add a related file path.

    Args:
        relative: the path to which you need to pick up a related path.
    Returns:
        relative path
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

ICON = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'icon.ico')))

BACKGROUND = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'backgr.png')))

USR_WIDTH = 90
USR_HEIGHT = 80
USR_X = DISPLAY_WIDTH // 3
PRIME_USR_Y = DISPLAY_HEIGHT - USR_HEIGHT - 82

BARRIER_IMG = [
    pygame.image.load(resource_path(os.path.join('C:/Games/Magic Rush/src/assets/barriers', 'barr0.png'))),
    pygame.image.load(resource_path(os.path.join('C:/Games/Magic Rush/src/assets/barriers', 'barr1.png'))),
    pygame.image.load(resource_path(os.path.join('C:/Games/Magic Rush/src/assets/barriers', 'barr2.png')))]

BARRIER_OPTIONS = [[70, 478],
                   [40, 468],
                   [30, 448]]  # ширина и высота относительно дисплея для каждого барьера

WIZARD_IMG = [pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/character', 'wizard0.png'))),
    pygame.image.load(
        resource_path(os.path.join('C:/Games/Magic Rush/src/assets/character', 'wizard1.png'))),
    pygame.image.load(
        resource_path(os.path.join('C:/Games/Magic Rush/src/assets/character', 'wizard2.png'))),
    pygame.image.load(
        resource_path(os.path.join('C:/Games/Magic Rush/src/assets/character', 'wizard3.png')))]

HEALTH_IMG = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/objects', 'heart_40.png')))
HEALTH_MINI_IMG = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/objects', 'heart_30.png')))

FONT_COLOR = (72, 10, 79)
FONT_TYPE = resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'font.ttf'))

CLOCK = pygame.time.Clock()

MENU_BACKGR = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'menu.png')))
REC_BACKGR = pygame.image.load(
    resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'table.png')))

MENU_MUSIC = resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'menu_music.mp3'))
MUSIC = resource_path(os.path.join('C:/Games/Magic Rush/src/assets/background', 'music.mp3'))