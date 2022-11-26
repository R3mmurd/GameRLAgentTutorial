from typing import TypeVar

from gale.state_machine import BaseState, StateMachine
from game.src.InputHandler import InputHandler

class IdleState(BaseState):
    def __init__(self, character: TypeVar('MainCharacter'), state_machine: StateMachine) -> None:
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction: str) -> None:
        self.direction = direction
        self.character.change_animation(f'idle-{self.direction}')

    def update(self, dt: float) -> None:
        InputHandler.handle_input(self.character)
