from typing import List

from pygame.surface import Surface
from pygame.rect import Rect

def generate_quads(atlas: Surface, tile_width: int, tile_height: int) -> List[Rect]:
    atlas_width, atlas_height = atlas.get_size()

    num_cols = atlas_width // tile_width
    num_rows = atlas_height // tile_height

    spritesheet = []
    for i in range(num_rows):
        for j in range(num_cols):
            spritesheet.append(
                Rect(
                    j * tile_width,
                    i * tile_height,
                    tile_width,
                    tile_height
                )
            )
    return spritesheet
