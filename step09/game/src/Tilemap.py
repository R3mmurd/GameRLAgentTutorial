from typing import Tuple

from pygame.surface import Surface

from game import settings
from game.src.mixins import DrawableMixin

class Tile(DrawableMixin):
    def __init__(self, x: int, y: int, frame: str) -> None:
        self.x = x
        self.y = y
        self.texture = 'tiles'
        self.frame = frame
        self.busy = False

class TileMap:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.map = [[None for _ in range(cols)] for _ in range(rows)]
        self.tiles = [[None for _ in range(cols)] for _ in range(rows)]

        self.width = cols * settings.TILE_SIZE
        self.height = rows * settings.TILE_SIZE

    @staticmethod
    def to_map(x: int, y: int) -> Tuple[int, int]:
        return TileMap.to_i(y), TileMap.to_j(x)

    @staticmethod
    def to_i(y: int) -> int:
        return int(y // settings.TILE_SIZE)
    
    @staticmethod
    def to_j(x: int) -> int:
        return int(x // settings.TILE_SIZE)

    @staticmethod
    def to_screen(i: int, j: int) -> Tuple[int, int]:
        return TileMap.to_x(j), TileMap.to_y(i)

    @staticmethod
    def to_x(j: int) -> int:
        return j * settings.TILE_SIZE
    
    @staticmethod
    def to_y(i: int) -> int:
        return i * settings.TILE_SIZE
    
    def render(self, surface: Surface) -> None:
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.render(surface)
        