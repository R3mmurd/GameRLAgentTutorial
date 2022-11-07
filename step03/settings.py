import pygame

from src.quad_utils import generate_quads

ENVIRONMENT_PATH = 'environments/01.txt'

# Size of our actual window
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 800

# Size we're trying to emulate
VIRTUAL_WIDTH = 80
VIRTUAL_HEIGHT = 96

TILE_SIZE = 16

pygame.mixer.init()

# Sound effects and music
GAME_SOUNDS = {
    'selected': pygame.mixer.Sound('sounds/selected.wav'),
}

# Graphics
GAME_TEXTURES = {
    'background': pygame.image.load('graphics/background.png'),
    'tiles': pygame.image.load('graphics/sheet.png'),
}

# Frames
GAME_FRAMES = {
    'tiles': generate_quads(GAME_TEXTURES['tiles'], TILE_SIZE, TILE_SIZE),
}

pygame.font.init()

# Fonts
GAME_FONTS = {
    'large': pygame.font.Font('fonts/font.ttf', 8),
}

# Dictionary of pressed keys
pressed_keys = {}
