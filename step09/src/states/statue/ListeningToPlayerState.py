from gale.state_machine import BaseState

class ListeningToPlayerState(BaseState):
    def __init__(self, statue, state_machine):
        super().__init__(state_machine)
        self.statue = statue

    def enter(self):
        self.statue.change_animation('listening')
