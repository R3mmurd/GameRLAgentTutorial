from game.src.InputHandler import Action
from game.src.Tilemap import TileMap
from game.src.Entity import Entity

class MoveLeftAction(Action):
    def execute(self, entity: Entity) -> None:
        tile_map = entity.tile_map
        i, j = TileMap.to_map(entity.x, entity.y)
        if j > 0 and tile_map.map[i][j - 1] != 0 and not tile_map.tiles[i][j - 1].busy:
            off_set = -1
        else:
            off_set = 0
        x, y = TileMap.to_screen(i, j + off_set)
        entity.state_machine.change('walking', 'left', (x, y))
        entity.game_level.statue_1.on_player_movement('left')
        entity.game_level.statue_2.on_player_movement('left')
