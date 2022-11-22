
class GameController:
    K_ENTER = 'enter'
    K_UP = 'up'
    K_RIGHT = 'right'
    K_DOWN = 'down'
    K_LEFT = 'left'

    def execute(self, action):
        raise NotImplementedError
