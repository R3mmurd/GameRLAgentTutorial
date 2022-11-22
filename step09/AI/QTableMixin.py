import random

class QTableMixin:
    MODE_EXPLORATION = 'exploration'
    MODE_EXPLOTATION = 'explotation'

    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1, default_value = 0):
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.default_value = default_value
        self.mode = None

    def get_available_actions(self):
        raise NotImplementedError
    
    def get_value(self, state, action):
        k = (state, action)
        return self.q.get(k, self.default_value)

    def set_value(self, state, action, value):
       k = (state, action) 
       self.q[k] = value

    def get_action(self, state):
        available_actions = self.get_available_actions()

        if self.mode == self.MODE_EXPLORATION and random.random() < self.epsilon:
            return random.choice(available_actions)

        best_action = available_actions[0]

        for current_action in available_actions[1:]:
            if self.get_value(state, current_action) > self.get_value(state, best_action):
                best_action = current_action

        return best_action

    def best_future_value(self, future_state):
        available_actions = self.get_available_actions()

        if len(available_actions) == 0:
            return 0

        best_value = self.get_value(future_state, available_actions[0])

        for action in available_actions[1:]:
            value = self.get_value(future_state, action)
            best_value = max(best_value, value)
        
        return best_value
    