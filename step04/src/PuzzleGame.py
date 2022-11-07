import pygame

from gale.game import Game
from gale.state_machine import StateMachine

import settings

import src.states.game as game_states

class PuzzleGame(Game):
    def init(self):
        self.state_machine = StateMachine({
            'initial': game_states.InitialState,
            'playing': game_states.PlayingState,
            'finish': game_states.FinishState
        })
        self.state_machine.change('initial')

    def update(self, dt):
        self.state_machine.update(dt)

    def render(self, surface):
        self.state_machine.render(surface)

    def keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.quit()
        settings.pressed_keys[key] = True
