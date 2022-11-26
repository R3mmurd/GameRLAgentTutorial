from typing import Tuple, TypeVar

from gale.timer import Timer
from gale.state_machine import BaseState, StateMachine

from game.src.Tilemap import TileMap

from game import settings

class WalkingState(BaseState):
    def __init__(self, character: TypeVar('MainCharacter'), state_machine: StateMachine) -> None:
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction: str, target: Tuple[int, int]) -> None:
        self.direction = direction
        self.character.change_animation(f'walk-{self.direction}')
        i, j = TileMap.to_map(self.character.x, self.character.y)

        def arrive() -> None:
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
