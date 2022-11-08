import settings

from src.Entity import Entity
from src.states.main_character import IdleState, WalkingState


class MainCharacter(Entity):
    def __init__(self, x, y, game_level):
        super().__init__(
            x, y, 
            settings.PLAYER_WIDTH,
            settings.PLAYER_HEIGHT,
            'main_character',
            game_level,
            states={
                'idle': lambda sm: IdleState(self, sm),
                'walking': lambda sm: WalkingState(self, sm),
            },
            animations={
                'walk-up': {
                    'frames': [0, 1, 2],
                    'interval': 0.1,
                },
                'walk-right': {
                    'frames': [3, 4, 5],
                    'interval': 0.1,
                },
                'walk-down': {
                    'frames': [6, 7, 8],
                    'interval': 0.1,
                },
                'walk-left': {
                    'frames': [9, 10, 11],
                    'interval': 0.1,
                },
                'idle-up': {
                    'frames': [1]
                },
                'idle-right': {
                    'frames': [4]
                },
                'idle-down': {
                    'frames': [7]
                },
                'idle-left': {
                    'frames': [11]
                },
            }
        )
        self.state_machine.change('idle', 'down')
