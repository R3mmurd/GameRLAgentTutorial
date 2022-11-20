from gale.state_machine import StateMachine

class GameStateMachine(StateMachine):
    def get_state_info(self):
        return self.current.get_state_info()
