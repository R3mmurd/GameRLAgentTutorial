from typing import Tuple, Optional

import pygame
from pygame.surface import Surface

from gale.timer import Timer
from gale.text import render_text

from game.src.states.game.BaseGameState import BaseGameState
from game.src.GameLevel import GameLevel

from game import settings

class FinishState(BaseGameState):
    def enter(self, finish_message: str, level: GameLevel) -> None:
        self.finish_message = finish_message
        self.level = level
        self.alpha = 0
        self.text = ''

        def fade_down_finish():
            self.text = f'You {self.finish_message}'

        Timer.tween(
            2,
            [(self, { 'alpha': 255 })],
            on_finish=fade_down_finish
        )

    def update(self, dt: float) -> None:
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change("initial")
    
    def render(self, surface: Surface) -> None:
        self.level.render(surface)
        r = pygame.Surface((settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA)
        r.fill((0, 0, 0, self.alpha))
        surface.blit(r, (0, 0))
        render_text(
            surface, self.text, settings.GAME_FONTS['large'], 
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2, 
            (255, 255, 255), center=True
        )

    def get_state_info(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        return (str(self), None, None, None, self.finish_message)
    
    def __str__(self):
        return 'Finish'
