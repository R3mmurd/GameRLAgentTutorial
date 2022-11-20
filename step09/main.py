import sys
import threading

from game import settings

from adapters import GraphicGameController, TrainingGameController
from training_game.TrainingGame import TrainingGame

from game.src.PuzzleGame import PuzzleGame
from AI.PlayerAgent import PlayerAgent

def get_state(game):
    return game.get_state_info()

def get_available_actions(game):
    state_name, _, _, _, _ = game.get_state_info()
    if state_name == "Initial":
        return ("enter",)
    elif state_name == "Playing":
        return ("up", "right", "down", "left")
    else:
        return tuple()

def get_reward(game):
    state_name, _, _, _, message = game.get_state_info()

    if state_name == "Initial":
        return 0
    elif state_name == "Playing":
        return -1
    else:
        return 1000 if message == "Won" else -100

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
    agent = PlayerAgent(
        get_state_function=get_state,
        get_available_actions_function=get_available_actions,
        get_reward_function=get_reward,
        alpha=0.1,
        gamma=0.9,
        epsilon=1
    )

    training_game = TrainingGame()
    agent.train(training_game, TrainingGameController(training_game), n)

    game = get_new_game()
    agent_thread = threading.Thread(target=start_agent_play_game, args=(agent, game, GraphicGameController(1.1)))
    agent_thread.start()
    game.exec()
    
    agent_thread.join()
    