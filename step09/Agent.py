import random
import time

import pyautogui

import settings

class TrainingController:
    def __init__(self, game):
        self.game = game
        self.actions = {
            'enter': self.game.press_enter,
            'up': self.game.move_up,
            'right': self.game.move_right,
            'down': self.game.move_down,
            'left': self.game.move_left,
        }
    
    def press(self, action):
        self.actions[action]()

class GameController():
    def press(self, action):
        pyautogui.press(action)
        time.sleep(1.1)

class Agent:
    MODE_EXPLORATION = 'exploration'
    MODE_EXPLOTATION = 'explotation'

    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
        self.game = None
        self.game_finished = False
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon 
        self.mode = None
        self.controller = None
 
    def _best_future_value(self, new_state):
        available_actions = self.game.get_available_actions()

        if len(available_actions) == 0:
            return 0

        best_value = self._get_q_value(new_state, available_actions[0])

        for action in available_actions[1:]:
            value = self._get_q_value(new_state, action)
            best_value = max(best_value, value)
        
        return best_value

    def _get_q_value(self, state, action):
        return self.q.get((state, action), 0)
    
    def _set_q_value(self, state, action, value):
        self.q[(state, action)] = value

    def _update_q_value(self, state, action, r, new_state):
        old_value = self._get_q_value(state, action)
        best_future = self._best_future_value(new_state)
        new_value = old_value + self.alpha * (r + self.gamma * best_future - old_value)
        self._set_q_value(state, action, new_value)

    def _get_state(self):
        state = self.game.get_state()
        return state

    def _choose_action(self, state):
        available_actions = self.game.get_available_actions()

        if self.mode == self.MODE_EXPLORATION and random.random() < self.epsilon:
            return random.choice(available_actions)

        best_action = available_actions[0]

        for curr_action in available_actions[1:]:
            if self._get_q_value(state, curr_action) > self._get_q_value(state, best_action):
                best_action = curr_action

        return best_action

    def _take_action(self, action):
        old_state = self.game.get_state()
        self.controller.press(action)
        return self._learn(old_state, action)

    def _learn(self, old_state, action):
        new_state = self.game.get_state()
        reward = self.game.get_reward()

        if reward == 0:
            reward = -1
            
        self._update_q_value(old_state, action, reward, new_state)

        if new_state[0] == 'Finish':
            self.game_finished = True
        
        return reward

    def step(self):
        state = self._get_state()
        action = self._choose_action(state)
        return self._take_action(action)

    def train(self, game, num_iterations):
        self.game = game
        self.mode = self.MODE_EXPLORATION
        self.controller = TrainingController(self.game)
        lost = 0
        won = 0
        result = 0
        for i in range(num_iterations):
            print(f"Training game {i + 1}")
            while not self.game_finished:
                result = self.step()

            if result < 0:
                lost += 1
            else:
                won += 1
            self.game_finished = False
            self.controller.press('enter')
        
        print(self.q)
        print(f"Table size: {len(self.q)}")
        print(f"Won: {won}")
        print(f"Lost: {lost}")

    def play(self, game):
        self.game = game
        self.mode = self.MODE_EXPLOTATION
        self.controller = GameController()
        self.game_finished = False
        print(f"Playing game")
        while not self.game_finished:
            self.step()

    def run(self, num_iterations=0):
        # self.train(num_iterations)
        self.play()
