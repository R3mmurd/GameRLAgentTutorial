from gale.timer import Timer

import settings

from src.Tilemap import TileMap
from src.Entity import Entity
from src.states.statue.ListeningToPlayerState import ListeningToPlayerState

class Statue(Entity):
    def __init__(self, x, y, game_level, action):
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

    def undo_movement(self):
        self.off_set_i *= -1
        self.off_set_j *= -1
        self.move()


    def move(self):
        i, j = TileMap.to_map(self.x, self.y)
        self.tile_map.tiles[i][j].busy = False
        x, y = TileMap.to_screen(i + self.off_set_i, j + self.off_set_j)

        def arrive():
            self.tile_map.tiles[i + self.off_set_i][j + self.off_set_j].busy = True

        Timer.tween(
            0.5,
            [(self, { 'x': x, 'y': y })],
            on_finish=arrive
        )
    
    def move_right(self):
        i, j = TileMap.to_map(self.x, self.y)
        if j < self.tile_map.cols - 1 and self.tile_map.map[i][j + 1] != 0 and not self.tile_map.tiles[i][j + 1].busy:
            self.off_set_i = 0
            self.off_set_j = 1
            self.move()

    def move_left(self):
        i, j = TileMap.to_map(self.x, self.y)
        if j > 0 and self.tile_map.map[i][j - 1] != 0 and not self.tile_map.tiles[i][j - 1].busy:
            self.off_set_i = 0
            self.off_set_j = -1
            self.move()
    
    def move_up(self):
        i, j = TileMap.to_map(self.x, self.y)
        if i > 0 and self.tile_map.map[i - 1][j] != 0 and not self.tile_map.tiles[i - 1][j].busy:
            self.off_set_i = -1
            self.off_set_j = 0
            self.move()

    def move_down(self):
        i, j = TileMap.to_map(self.x, self.y)
        if i < self.tile_map.rows - 1 and self.tile_map.map[i + 1][j] != 0 and not self.tile_map.tiles[i + 1][j].busy:
            self.off_set_i = 1
            self.off_set_j = 0
            self.move()

        

    def on_player_movement(self, direction):
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
