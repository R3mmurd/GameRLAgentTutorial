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

    def available_actions(self):
        return ('up', 'right', 'left', 'down')

    def __str__(self):
        return 'Playing'