from src.InputHandler import Action
from src.Tilemap import TileMap

class MoveDownAction(Action):
    def execute(self, entity):
        tile_map = entity.tile_map
        i, j = TileMap.to_map(entity.x, entity.y)
        if i < tile_map.rows - 1 and tile_map.map[i + 1][j] != 0:
            off_set = 1
        else:
            off_set = 0
        x, y = TileMap.to_screen(i + off_set, j)
        entity.state_machine.change('walking', 'down', (x, y))
