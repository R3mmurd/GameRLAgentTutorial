from gale.state_machine import BaseState

class BaseGameState(BaseState):
    def get_state(self):
        return (str(self), None, None, None, None, None)

    def available_actions(self):
        return tuple()

    def reward(self):
        return 0
    
    def __str__(self):
        return 'Base'
