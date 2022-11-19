from AI.AgentMixin import AgentMixin
from AI.QTableMixin import QTableMixin

class PlayerAgent(QTableMixin, AgentMixin):
    
    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
        super().__init__(alpha, gamma, epsilon)
        self.game = None
        self.game_finished = False
        self.controller = None

    def get_available_actions(self):
        return self.game.get_available_actions()    

    def get_state(self):
        state = self.game.get_state()
        return state

    def take_action(self, action):
        self.controller.execute(action)
        return self.get_state()

    def learn(self, old_state, action, new_state):
        reward = self.game.get_reward()

        if reward == 0:
            reward = -1
            
        self.update_q_value(old_state, action, reward, new_state)

        if new_state[0] == 'Finish':
            self.game_finished = True
        
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
