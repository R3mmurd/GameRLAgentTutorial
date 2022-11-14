import sys
import threading

import settings

from training_game import TrainingGame

from src.PuzzleGame import PuzzleGame
from Agent import Agent

def run_agent(agent, game):
    agent.play(game)

def get_new_game():
    return PuzzleGame(
        title='Puzzle Game',
        window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )

if __name__ == '__main__':
    n = 50 if len(sys.argv) < 2 else int(sys.argv[1])
    agent = Agent(0.1, 0.9, 1)
    agent.train(TrainingGame(), n)

    game = get_new_game()
    agent_thread = threading.Thread(target=run_agent, args=(agent, game))
    agent_thread.start()
    game.exec()
    
    agent_thread.join()