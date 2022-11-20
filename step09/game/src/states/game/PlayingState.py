from game import settings

from game.src.states.game.BaseGameState import BaseGameState
from game.src.GameLevel import GameLevel
from game.src.Tilemap import TileMap

class PlayingState(BaseGameState):
    def enter(self):
        self.level = GameLevel()

    def update(self, dt):
        self.level.update(dt)
        if self.level.finish:
            self.state_machine.change('finish', self.level.finish, self.level)

    def render(self, surface):
        self.level.render(surface)

    def get_state_info(self):
        player_pos = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1_pos = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2_pos = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return (str(self), player_pos, s1_pos, s2_pos, None)

    def __str__(self):
        return 'Playing'