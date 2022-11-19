import sys
import threading

from game import settings

from adapters import GraphicGameController, TrainingGameController
from training_game.TrainingGame import TrainingGame

from game.src.PuzzleGame import PuzzleGame
from AI.PlayerAgent import PlayerAgent

def start_agent_play_game(agent, game, game_controller):
    agent.play(game, game_controller)

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
    agent = PlayerAgent(0.1, 0.9, 1)

    training_game = TrainingGame()
    agent.train(training_game, TrainingGameController(training_game), n)

    game = get_new_game()
    agent_thread = threading.Thread(target=start_agent_play_game, args=(agent, game, GraphicGameController(1.1)))
    agent_thread.start()
    game.exec()
    
    agent_thread.join()
    