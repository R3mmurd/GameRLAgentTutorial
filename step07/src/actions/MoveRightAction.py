from src.InputHandler import Action
from src.Tilemap import TileMap

class MoveRightAction(Action):
    def execute(self, entity):
        tile_map = entity.tile_map
        i, j = TileMap.to_map(entity.x, entity.y)
        if j < tile_map.cols - 1 and tile_map.map[i][j + 1] != 0 and not tile_map.tiles[i][j + 1].busy:
            off_set = 1
        else:
            off_set = 0
        x, y = TileMap.to_screen(i, j + off_set)
        entity.state_machine.change('walking', 'right', (x, y))
        entity.game_level.statue_1.on_player_movement('right')
        entity.game_level.statue_2.on_player_movement('right')
        