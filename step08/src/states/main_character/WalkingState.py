from gale.timer import Timer
from gale.state_machine import BaseState

from src.Tilemap import TileMap

class WalkingState(BaseState):
    def __init__(self, character, state_machine):
        super().__init__(state_machine)
        self.character = character
        self.direction = None
    
    def enter(self, direction, target):
        self.direction = direction
        self.character.change_animation(f'walk-{self.direction}')
        i, j = TileMap.to_map(self.character.x, self.character.y)
        self.character.tile_map.tiles[i][j].busy = False

        def arrive():
            self.character.state_machine.change('idle', self.direction)
            i, j = TileMap.to_map(self.character.x, self.character.y)
            self.character.tile_map.tiles[i][j].busy = True
            self.character

        Timer.tween(
            0.5,
            [(self.character, { 'x': target[0], 'y': target[1] })],
            on_finish=arrive
        )
