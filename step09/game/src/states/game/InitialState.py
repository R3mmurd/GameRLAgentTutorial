import pygame
from pygame.surface import Surface

from gale.text import render_text

from game.src.states.game.BaseGameState import BaseGameState

from game import settings

class InitialState(BaseGameState):
    def update(self, dt: float) -> None:
        if settings.pressed_keys.get(pygame.K_RETURN):
            settings.GAME_SOUNDS['selected'].play()
            self.state_machine.change('playing')

    def render(self, surface: Surface) -> None:
        render_text(
            surface, 'Puzzle Game', settings.GAME_FONTS['large'],
             settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//3,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press enter', settings.GAME_FONTS['large'], 
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2, 
            (255, 255, 255), center=True
        )
    
    def __str__(self) -> str:
        return 'Initial'
