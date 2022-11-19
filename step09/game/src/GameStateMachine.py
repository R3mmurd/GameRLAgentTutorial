from gale.state_machine import StateMachine

class GameStateMachine(StateMachine):
    def get_state(self):
        return self.current.get_state()

    def available_actions(self):
        return self.current.available_actions()

    def reward(self):
        return self.current.reward()
