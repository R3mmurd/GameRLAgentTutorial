import pygame

# Size of our actual window
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 800

# Size we're trying to emulate
VIRTUAL_WIDTH = 80
VIRTUAL_HEIGHT = 96

pygame.mixer.init()

# Sound effects and music
GAME_SOUNDS = {
    'selected': pygame.mixer.Sound('sounds/selected.wav'),
}

# Graphics
GAME_TEXTURES = {}

# Frames
GAME_FRAMES = {}

pygame.font.init()

# Fonts
GAME_FONTS = {
    'large': pygame.font.Font('fonts/font.ttf', 8),
}

# Dictionary of pressed keys
pressed_keys = {}
