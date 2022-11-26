import pygame

from gale.game import Game

from game import settings

from game.src.GameStateMachine import GameStateMachine
import game.src.states.game as game_states
from game.src.InputHandler import InputHandler
from game.src.actions import MoveDownAction, MoveLeftAction, MoveRightAction, MoveUpAction

class PuzzleGame(Game):
    def init(self):
        self.state_machine = GameStateMachine({
            'initial': game_states.InitialState,
            'playing': game_states.PlayingState,
            'finish': game_states.FinishState
        })
        self.state_machine.change('initial')
        InputHandler.add_action(pygame.K_UP, MoveUpAction())
        InputHandler.add_action(pygame.K_DOWN, MoveDownAction())
        InputHandler.add_action(pygame.K_RIGHT, MoveRightAction())
        InputHandler.add_action(pygame.K_LEFT, MoveLeftAction())
        

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        settings.pressed_keys = {}

    def render(self, surface):
        self.state_machine.render(surface)

    def keydown(self, key: int) -> None:
        if key == pygame.K_ESCAPE:
            self.quit()
        settings.pressed_keys[key] = True

    def get_state_info(self):
        return self.state_machine.get_state_info()

