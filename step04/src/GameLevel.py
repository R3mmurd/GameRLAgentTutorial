import settings

from src.Tilemap import Tile, TileMap
from src.definitions import TILES

class GameLevel:
    def __init__(self):
        self.tile_map = None
        self._load_map()

    def _load_map(self):
        with open(settings.ENVIRONMENT_PATH, 'r') as f:
            rows, cols = f.readline().split(' ')
            rows, cols = int(rows), int(cols)
            self.tile_map = TileMap(rows, cols)

            for i in range(rows):
                row = f.readline()
                if row[-1] == '\n':
                    row = row[:-1]
                row = row.split(' ')

                for j in range(cols):
                    tile_def = TILES[row[j]]
                    x, y = TileMap.to_screen(i, j)
                    self.tile_map.tiles[i][j] = Tile(
                        x, y, tile_def['frame']
                    )
                    self.tile_map.map[i][j] = int(row(j))

    def render(self, surface):
        self.tile_map.render(surface)
