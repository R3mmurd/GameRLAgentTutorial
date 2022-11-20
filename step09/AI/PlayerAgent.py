from AI.AgentMixin import AgentMixin
from AI.QTableMixin import QTableMixin

class PlayerAgent(QTableMixin, AgentMixin):
    
    def __init__(self, get_state_function, get_available_actions_function, get_reward_function, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
        self.game = None
        self.game_finished = False
        self.controller = None
        self._get_state = get_state_function
        self._get_available_actions = get_available_actions_function
        self._get_reward = get_reward_function
        super().__init__(alpha, gamma, epsilon)

    def get_state(self):
        return self._get_state(self.game)

    def get_available_actions(self):
        return self._get_available_actions(self.game)

    def get_reward(self):
        return self._get_reward(self.game)

    def take_action(self, action):
        self.controller.execute(action)
        return self.get_state()

    def learn(self, old_state, action, new_state):
        reward = self.get_reward()

        self.update_q_value(old_state, action, reward, new_state)

        self.game_finished = new_state[0] == 'Finish' or not self.game.running
             
        return reward

    def train(self, game, game_controller, num_iterations):
        self.game = game
        self.controller = game_controller
        self.mode = self.MODE_EXPLORATION
        lost = 0
        won = 0
        result = 0

        for i in range(num_iterations):
            print(f"Training game {i + 1}")
            while not self.game_finished:
                _, _, _, result = self.step()

            if result < 0:
                lost += 1
            else:
                won += 1

            self.game_finished = False
            self.controller.execute('enter')
        
        print(self.q)
        print(f"Table size: {len(self.q)}")
        print(f"Won: {won}")
        print(f"Lost: {lost}")

    def play(self, game, game_controller):
        self.game = game
        self.controller = game_controller
        self.mode = self.MODE_EXPLOTATION
        self.game_finished = False
        print(f"Playing game")
        while not self.game_finished:
            self.step()
