from typing import TypeVar

from gale.timer import Timer

from game import settings

from game.src.Tilemap import TileMap
from game.src.Entity import Entity
from game.src.states.statue.ListeningToPlayerState import ListeningToPlayerState

class Statue(Entity):
    def __init__(self, x: int, y: int, game_level: TypeVar('GameLevel'), action: str) -> None:
        super().__init__(
            x, y, 
        
            settings.STATUE_WIDTH,
            settings.STATUE_HEIGHT,
            'statue',
            game_level,
            states={
                'listening': lambda sm: ListeningToPlayerState(self, sm),
            },
            animations={
                'listening': {
                    'frames': [0]
                }
            },
        )
        self.state_machine.change('listening')
        self.action = action
        self.off_set_i = 0
        self.off_set_j = 0

    def undo_movement(self) -> None:
        self.off_set_i *= -1
        self.off_set_j *= -1
        self.move()

    def move(self) -> None:
        i, j = TileMap.to_map(self.x, self.y)
        x, y = TileMap.to_screen(i + self.off_set_i, j + self.off_set_j)

        def arrive():
            self.tile_map.tiles[i][j].busy = False
            self.tile_map.tiles[i + self.off_set_i][j + self.off_set_j].busy = True

        Timer.tween(
            settings.movement_time,
            [(self, { 'x': x, 'y': y })],
            on_finish=arrive
        )
    
    def move_right(self) -> None:
        i, j = TileMap.to_map(self.x, self.y)
        if j < self.tile_map.cols - 1 and self.tile_map.map[i][j + 1] != 0 and not self.tile_map.tiles[i][j + 1].busy:
            self.off_set_i = 0
            self.off_set_j = 1
            self.move()

    def move_left(self) -> None:
        i, j = TileMap.to_map(self.x, self.y)
        if j > 0 and self.tile_map.map[i][j - 1] != 0 and not self.tile_map.tiles[i][j - 1].busy:
            self.off_set_i = 0
            self.off_set_j = -1
            self.move()
    
    def move_up(self) -> None:
        i, j = TileMap.to_map(self.x, self.y)
        if i > 0 and self.tile_map.map[i - 1][j] != 0 and not self.tile_map.tiles[i - 1][j].busy:
            self.off_set_i = -1
            self.off_set_j = 0
            self.move()

    def move_down(self) -> None:
        i, j = TileMap.to_map(self.x, self.y)
        if i < self.tile_map.rows - 1 and self.tile_map.map[i + 1][j] != 0 and not self.tile_map.tiles[i + 1][j].busy:
            self.off_set_i = 1
            self.off_set_j = 0
            self.move()

        

    def on_player_movement(self, direction: str) -> None:
        if direction == 'right':
            if self.action == 'follow':
                self.move_right()
            else:
                self.move_left()
        elif direction == 'left':
            if self.action == 'follow':
                self.move_left()
            else:
                self.move_right()
        elif direction == 'up':
            if self.action == 'follow':
                self.move_up()
            else:
                self.move_down()
        elif direction == 'down':
            if self.action == 'follow':
                self.move_down()
            else:
                self.move_up()
