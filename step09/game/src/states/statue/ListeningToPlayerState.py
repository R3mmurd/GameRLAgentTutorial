from typing import TypeVar

from gale.state_machine import BaseState, StateMachine

class ListeningToPlayerState(BaseState):
    def __init__(self, statue: TypeVar('Statue'), state_machine: StateMachine) -> None:
        super().__init__(state_machine)
        self.statue = statue

    def enter(self) -> None:
        self.statue.change_animation('listening')
