import pygame

from gale.state_machine import BaseState
from gale.text import render_text

import settings

class InitialState(BaseState):
    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            settings.GAME_SOUNDS['selected'].play()
            self.state_machine.change('playing')

    def render(self, surface):
        render_text(
            surface, 'Puzzle Game', settings.GAME_FONTS['large'],
             settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//3,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press enter to start', settings.GAME_FONTS['medium'], 
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT-60, 
            (255, 255, 255), center=True
        )
