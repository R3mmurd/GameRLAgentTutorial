from typing import Tuple, Optional

from pygame.surface import Surface

from game.src.states.game.BaseGameState import BaseGameState
from game.src.GameLevel import GameLevel
from game.src.Tilemap import TileMap

class PlayingState(BaseGameState):
    def enter(self) -> None:
        self.level = GameLevel()

    def update(self, dt: float) -> None:
        self.level.update(dt)
        if self.level.finish:
            self.state_machine.change('finish', self.level.finish, self.level)

    def render(self, surface: Surface) -> None:
        self.level.render(surface)

    def get_state_info(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        player_pos = TileMap.to_map(self.level.player.x, self.level.player.y)
        s1_pos = TileMap.to_map(self.level.statue_1.x, self.level.statue_1.y)
        s2_pos = TileMap.to_map(self.level.statue_2.x, self.level.statue_2.y)
        return (str(self), player_pos, s1_pos, s2_pos, None)

    def __str__(self):
        return 'Playing'