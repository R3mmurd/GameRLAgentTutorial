from gale.timer import Timer
from gale.state_machine import BaseState

class WalkingState(BaseState):
    def __init__(self, character, state_machine):
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction, target):
        self.direction = direction
        self.character.change_animation(f'walk-{self.direction}')
        Timer.tween(
            0.5,
            {
                self.character: {
                    'x': target[0],
                    'y': target[1]
                }
            },
            on_finish=lambda: self.character.state_machine.change('idle', self.direction)
        )
