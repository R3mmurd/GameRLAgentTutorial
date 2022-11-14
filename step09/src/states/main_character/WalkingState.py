from gale.timer import Timer
from gale.state_machine import BaseState

from src.Tilemap import TileMap

import settings

class WalkingState(BaseState):
    def __init__(self, character, state_machine):
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction, target):
        self.direction = direction
        self.character.change_animation(f'walk-{self.direction}')
        i, j = TileMap.to_map(self.character.x, self.character.y)

        def arrive():
            self.character.state_machine.change('idle', self.direction)
            i, j = TileMap.to_map(self.character.x, self.character.y)
            self.character

        Timer.tween(
            settings.movement_time,
            {
                self.character: {
                    'x': target[0],
                    'y': target[1]
                }
            },
            on_finish=arrive
        )
