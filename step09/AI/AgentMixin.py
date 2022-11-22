class AgentMixin:
    def get_state(self):
        raise NotImplementedError

    def get_action(self, state):
        raise NotImplementedError
    
    def take_action(self, action):
        raise NotImplementedError

    def learn(self, old_state, action, new_state):
        raise NotImplementedError

    def step(self):
        state = self.get_state()
        action = self.get_action(state)
        new_state = self.take_action(action)
        reward = self.learn(state, action, new_state)
        return (state, action, new_state, reward)
