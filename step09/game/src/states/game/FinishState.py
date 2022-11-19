import pygame

from gale.timer import Timer
from gale.text import render_text

from game.src.states.game.BaseGameState import BaseGameState

from game import settings

class FinishState(BaseGameState):
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

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change("initial")
    
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

    def reward(self):
        return 1000 if self.finish_message == 'Won' else -100

    def __str__(self):
        return 'Finish'
