import settings

from src.Tilemap import Tile, TileMap
from src.MainCharacter import MainCharacter
from src.definitions import TILES

class GameLevel:
    def __init__(self):
        self.tile_map = None
        self.player = None
        self._load_environment()

    def _load_environment(self):
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
            player_row, player_col = f.readline().split(' ')
            player_row, player_col = int(player_row), int(player_col)
            x, y = TileMap.to_screen(player_row, player_col)
            self.player = MainCharacter(x, y, self)

    def update(self, dt):
        self.player.update(dt)

    def render(self, surface):
        self.tile_map.render(surface)
        self.player.render(surface)
