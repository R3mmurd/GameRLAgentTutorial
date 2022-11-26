from typing import Tuple, Optional

from gale.state_machine import StateMachine

class GameStateMachine(StateMachine):
    def get_state_info(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        return self.current.get_state_info()
