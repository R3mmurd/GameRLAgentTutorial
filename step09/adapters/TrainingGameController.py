from adapters.GameController import GameController

class TrainingGameController:
    def __init__(self, game):
        self.game = game
        self.actions = {
            GameController.K_ENTER: self.game.press_enter,
            GameController.K_UP: self.game.move_up,
            GameController.K_RIGHT: self.game.move_right,
            GameController.K_DOWN: self.game.move_down,
            GameController.K_LEFT: self.game.move_left,
        }
    
    def execute(self, action):
        self.actions[action]()
