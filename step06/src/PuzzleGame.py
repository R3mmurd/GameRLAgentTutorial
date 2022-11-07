import pygame

from gale.game import Game
from gale.state_machine import StateMachine

import settings

import src.states.game as game_states

from src.InputHandler import InputHandler
from src.actions import MoveDownAction, MoveLeftAction, MoveRightAction, MoveUpAction

class PuzzleGame(Game):
    def init(self):
        self.state_machine = StateMachine({
            'initial': game_states.InitialState,
            'playing': game_states.PlayingState,
            'finish': game_states.FinishState
        })
        self.state_machine.change('initial')
        InputHandler.add_action(pygame.K_UP, MoveUpAction())
        InputHandler.add_action(pygame.K_DOWN, MoveDownAction())
        InputHandler.add_action(pygame.K_RIGHT, MoveRightAction())
        InputHandler.add_action(pygame.K_LEFT, MoveLeftAction())
        

    def update(self, dt):
        self.state_machine.update(dt)

    def render(self, surface):
        self.state_machine.render(surface)

    def keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.quit()
        settings.pressed_keys[key] = True
