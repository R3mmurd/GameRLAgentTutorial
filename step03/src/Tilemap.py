import settings

from src.mixins import DrawableMixin

class Tile(DrawableMixin):
    def __init__(self, x, y, frame):
        self.x = x
        self.y = y
        self.texture = 'tiles'
        self.frame = frame

class TileMap:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = [[None for _ in range(cols)] for _ in range(rows)]

        self.width = cols * settings.TILE_SIZE
        self.height = rows * settings.TILE_SIZE

    @staticmethod
    def to_map(x, y):
        return TileMap.to_i(y), TileMap.to_j(x)

    @staticmethod
    def to_i(y):
        return y // settings.TILE_SIZE
    
    @staticmethod
    def to_j(x):
        return x // settings.TILE_SIZE

    @staticmethod
    def to_screen(i, j):
        return TileMap.to_x(j), TileMap.to_y(i)

    @staticmethod
    def to_x(j):
        return j * settings.TILE_SIZE
    
    @staticmethod
    def to_y(i):
        return i * settings.TILE_SIZE
    
    def render(self, surface):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.render(surface)
        