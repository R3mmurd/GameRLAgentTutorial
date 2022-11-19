from adapters.GameController import GameController

class TrainingGameController:
    def __init__(self, game):
        self.game = game
        self.actions = {
            'enter': self.game.press_enter,
            'up': self.game.move_up,
            'right': self.game.move_right,
            'down': self.game.move_down,
            'left': self.game.move_left,
        }
    
    def execute(self, action):
        self.actions[action]()
