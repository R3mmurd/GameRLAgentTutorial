from typing import Tuple, Optional

from gale.state_machine import BaseState

class BaseGameState(BaseState):
    def get_state_info(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        return (str(self), None, None, None, None)
    
    def __str__(self) -> str:
        return 'Base'
