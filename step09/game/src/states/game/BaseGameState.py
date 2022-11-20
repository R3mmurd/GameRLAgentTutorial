from gale.state_machine import BaseState

class BaseGameState(BaseState):
    def get_state_info(self):
        return (str(self), None, None, None, None)
    
    def __str__(self):
        return 'Base'
