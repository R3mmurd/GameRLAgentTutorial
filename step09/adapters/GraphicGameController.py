import time

import pyautogui

from adapters.GameController import GameController

class GraphicGameController(GameController):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def execute(self, action):
        pyautogui.press(action)
        time.sleep(self.sleep_time)
