from gale.state_machine import BaseState
from game.src.InputHandler import InputHandler

class IdleState(BaseState):
    def __init__(self, character, state_machine):
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction):
        self.direction = direction
        self.character.change_animation(f'idle-{self.direction}')

    def update(self, dt):
        InputHandler.handle_input(self.character)
