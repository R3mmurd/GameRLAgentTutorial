import pygame

from game.src.quad_utils import generate_quads

ENVIRONMENT_PATH = 'environments/01.txt'

# Size of our actual window
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 800

# Size we're trying to emulate
VIRTUAL_WIDTH = 80
VIRTUAL_HEIGHT = 96

TILE_SIZE = 16
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 18
STATUE_WIDTH = 16
STATUE_HEIGHT = 21

pygame.mixer.init()

# Sound effects and music
GAME_SOUNDS = {
    'selected': pygame.mixer.Sound('game/sounds/selected.wav'),
}

# Graphics
GAME_TEXTURES = {
    'background': pygame.image.load('game/graphics/background.png'),
    'tiles': pygame.image.load('game/graphics/sheet.png'),
    'main_character': pygame.image.load('game/graphics/main_character.png'),
    'statue': pygame.image.load('game/graphics/ghost.png'),
}

# Frames
GAME_FRAMES = {
    'tiles': generate_quads(GAME_TEXTURES['tiles'], TILE_SIZE, TILE_SIZE),
    'main_character': generate_quads(GAME_TEXTURES['main_character'], PLAYER_WIDTH, PLAYER_HEIGHT),
    'statue': generate_quads(GAME_TEXTURES['statue'], STATUE_WIDTH, STATUE_HEIGHT),
}

pygame.font.init()

# Fonts
GAME_FONTS = {
    'large': pygame.font.Font('game/fonts/font.ttf', 8),
}

# Dictionary of pressed keys
pressed_keys = {}

movement_time = 0.5