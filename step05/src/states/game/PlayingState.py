from gale.state_machine import BaseState

import settings

from src.GameLevel import GameLevel

class PlayingState(BaseState):
    def enter(self):
        self.level = GameLevel()

    def update(self, dt):
        self.level.update(dt)

    def render(self, surface):
        surface.blit(
            settings.GAME_TEXTURES['background'], (0, 0)
        )
        self.level.render(surface)
