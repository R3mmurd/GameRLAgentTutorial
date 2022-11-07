from src.InputHandler import Action
from src.Tilemap import TileMap

class MoveLeftAction(Action):
    def execute(self, entity):
        tile_map = entity.tile_map
        i, j = TileMap.to_map(entity.x, entity.y)
        if j > 0 and tile_map.map[i][j - 1] != 0:
            off_set = -1
        else:
            off_set = 0
        x, y = TileMap.to_screen(i, j + off_set)
        entity.state_machine.change('walking', 'left', (x, y))
