import settings

from src.Tilemap import Tile, TileMap
from src.MainCharacter import MainCharacter
from src.Statue import Statue
from src.definitions import TILES

class GameLevel:
    def __init__(self):
        self.tile_map = None
        self.player = None
        self.statue_1 = None
        self.statue_2 = None
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
                    self.tile_map.map[i][j] = int(row[j])
                    
            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.player = MainCharacter(x, y, self)
            self.tile_map.tiles[row][col].busy = True

            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.statue_1 = Statue(x, y, self, 'follow')
            self.tile_map.tiles[row][col].busy = True

            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            x, y = TileMap.to_screen(row, col)
            self.statue_2 = Statue(x, y, self, 'mirror')
            self.tile_map.tiles[row][col].busy = True

    def update(self, dt):
        self.player.update(dt)
        self.statue_1.update(dt)
        self.statue_2.update(dt)

        if self.statue_1.x == self.statue_2.x and self.statue_1.y == self.statue_2.y:
            self.statue_1.undo_movement()
            self.statue_2.undo_movement()

    def render(self, surface):
        self.tile_map.render(surface)
        self.player.render(surface)
        self.statue_1.render(surface)
        self.statue_2.render(surface)
