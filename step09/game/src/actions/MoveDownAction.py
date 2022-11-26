from game.src.InputHandler import Action
from game.src.Tilemap import TileMap
from game.src.Entity import Entity

class MoveDownAction(Action):
    def execute(self, entity: Entity) -> None:
        tile_map = entity.tile_map
        i, j = TileMap.to_map(entity.x, entity.y)
        if i < tile_map.rows - 1 and tile_map.map[i + 1][j] != 0 and not tile_map.tiles[i + 1][j].busy:
            off_set = 1
        else:
            off_set = 0
        x, y = TileMap.to_screen(i + off_set, j)
        entity.state_machine.change('walking', 'down', (x, y))
        entity.game_level.statue_1.on_player_movement('down')
        entity.game_level.statue_2.on_player_movement('down')
