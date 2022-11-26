from typing import Callable, Union, Tuple, Optional

from AI.AgentMixin import AgentMixin
from AI.QTableMixin import QTableMixin

class PlayerAgent(QTableMixin, AgentMixin):
    def __init__(
        self,
        get_state_function: Callable,
        get_available_actions_function: Callable,
        get_reward_function: Callable,
        alpha: float = 0.1,
        gamma: float = 0.9,
        epsilon: float = 0.1
    ):
        self.game = None
        self.game_finished = False
        self.controller = None
        self._get_state = get_state_function
        self._get_available_actions = get_available_actions_function
        self._get_reward = get_reward_function
        super().__init__(alpha, gamma, epsilon)

    def get_state(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        return self._get_state(self.game)

    def get_available_actions(self) -> Tuple[str]:
        return self._get_available_actions(self.game)

    def get_reward(self) -> float:
        return self._get_reward(self.game)

    def take_action(self, action) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        self.controller.execute(action)
        return self.get_state()

    def learn(
        self, 
        old_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]], 
        action: str,
        new_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]
    ) -> float:
        reward = self.get_reward()
        self.update_q_value(old_state, action, reward, new_state)
        return reward
    
    def update_q_value(
        self, 
        current_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]],
        current_action: str,
        reward: float,
        future_state: Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]
    ) -> None:
        old_value = self.get_value(current_state, current_action)
        best_future_value = self.best_future_value(future_state)
        new_value = old_value + self.alpha * (reward + self.gamma * best_future_value - old_value)
        self.set_value(current_state, current_action, new_value)
