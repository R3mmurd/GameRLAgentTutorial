import pygame

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we're trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

pygame.mixer.init()

# Sound effects and music
GAME_SOUNDS = {
    'selected': pygame.mixer.Sound('sounds/selected.wav'),
}

# Graphics
GAME_TEXTURES = {}

pygame.font.init()

# Fonts
GAME_FONTS = {
    'small': pygame.font.Font('fonts/font.ttf', 8),
    'medium': pygame.font.Font('fonts/font.ttf', 12),
    'large': pygame.font.Font('fonts/font.ttf', 24),
}

# Dictionary of pressed keys
pressed_keys = {}
