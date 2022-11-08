from gale.state_machine import BaseState

import settings

from src.GameLevel import GameLevel

class PlayingState(BaseState):
    def enter(self):
        self.level = GameLevel()

    def update(self, dt):
        self.level.update(dt)
        if self.level.finish:
            self.state_machine.change('finish', self.level.finish, self.level)

    def render(self, surface):
        self.level.render(surface)
