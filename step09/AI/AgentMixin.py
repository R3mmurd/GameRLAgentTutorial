from typing import Optional, Tuple

class AgentMixin:
    def get_state(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        raise NotImplementedError

    def get_action(self, state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]) -> str:
        raise NotImplementedError
    
    def take_action(self, action: str) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        raise NotImplementedError

    def learn(self,
              old_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]],
              action: str,
              new_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]
    ) -> float:
        raise NotImplementedError

    def step(self):
        state = self.get_state()
        action = self.get_action(state)
        new_state = self.take_action(action)
        reward = self.learn(state, action, new_state)
        return (state, action, new_state, reward)
