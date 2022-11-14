import settings

from src.states.game.BaseGameState import BaseGameState
from src.GameLevel import GameLevel

from src.Tilemap import TileMap

class PlayingState(BaseGameState):
    def enter(self):
        self.level = GameLevel()

    def update(self, dt):
        self.level.update(dt)
        if self.level.finish:
            self.state_machine.change('finish', self.level.finish, self.level)

    def render(self, surface):
        self.level.render(surface)

    def get_state(self):
        player_pos = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1_pos = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2_pos = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return (str(self), player_pos, s1_pos, s2_pos, self.level.target_1, self.level.target_2)

    def can_go(self, i, j):
        return i >= 0 and j >= 0 and i < self.level.tile_map.rows and j < self.level.tile_map.cols and not self.level.tile_map.tiles[i][j].busy and self.level.tile_map.map[i][j] != 0

    def can_move_up(self):
        pi, pj = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1i, s1j = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2i, s2j = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return self.can_go(pi - 1, pj) or self.can_go(s1i + 1, s1j) or self.can_go(s2i - 1, s2j)
    
    def can_move_down(self):
        pi, pj = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1i, s1j = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2i, s2j = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return self.can_go(pi + 1, pj) or self.can_go(s1i - 1, s1j) or self.can_go(s2i + 1, s2j)
    
    def can_move_right(self):
        pi, pj = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1i, s1j = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2i, s2j = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return self.can_go(pi, pj + 1) or self.can_go(s1i, s1j - 1) or self.can_go(s2i, s2j + 1)
    
    def can_move_left(self):
        pi, pj = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1i, s1j = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2i, s2j = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return self.can_go(pi, pj - 1) or self.can_go(s1i, s1j + 1) or self.can_go(s2i, s2j - 1)

    def available_actions(self):
        result = []

        if self.can_move_up():
            result.append('up')

        if self.can_move_down():
            result.append('down')

        if self.can_move_right():
            result.append('right')

        if self.can_move_left():
            result.append('left')

        return tuple(result)

    def __str__(self):
        return 'Playing'