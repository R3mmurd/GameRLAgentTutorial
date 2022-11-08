import pygame

from gale.state_machine import BaseState
from gale.timer import Timer
from gale.text import render_text

import settings

class FinishState(BaseState):
    def enter(self, finish_message, level):
        self.finish_message = finish_message
        self.level = level
        self.alpha = 0
        self.text = ''

        def fade_down_finish():
            self.text = f'You {self.finish_message}'

        Timer.tween(
            2,
            {
                self: {
                    'alpha': 255
                }
            },
            on_finish=fade_down_finish
        )
    
    def render(self, surface):
        self.level.render(surface)
        r = pygame.Surface((settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA)
        r.fill((0, 0, 0, self.alpha))
        surface.blit(r, (0, 0))
        render_text(
            surface, self.text, settings.GAME_FONTS['large'], 
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2, 
            (255, 255, 255), center=True
        )