"""
This program integrates the agent with the training game and
the graphic game and the controller adapters to play them.
"""

import sys
import threading

from typing import Tuple, Optional, Union

from game import settings

from adapters import GameController, GraphicGameController, TrainingGameController
from training_game.TrainingGame import TrainingGame

from game.src.PuzzleGame import PuzzleGame
from AI.PlayerAgent import PlayerAgent


"""
Get the state information from the game

This function will be used by the agent.
"""
def get_state(game: Union[TrainingGame, PuzzleGame]) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
    return game.get_state_info()

"""
Get the available actions from the game according to its state.

This function will be used by the agent.
"""
def get_available_actions(game: Union[TrainingGame, PuzzleGame]) -> Tuple[str]:
    state_name, _, _, _, _ = game.get_state_info()
    if state_name == "Initial":
        return (GameController.K_ENTER,)
    elif state_name == "Playing":
        return (GameController.K_UP, GameController.K_RIGHT, GameController.K_DOWN, GameController.K_LEFT)
    else:
        return tuple()


"""
Get the reward from the game according to its state.

This function will be used by the agent.
"""
def get_reward(game: Union[TrainingGame, PuzzleGame]) -> float:
    state_name, _, _, _, message = game.get_state_info()

    if state_name == "Initial":
        return 0
    elif state_name == "Playing":
        return -1
    else:
        return 1000 if message == "Won" else -100


"""
Train an agent to learn to play a game with a given controller.
"""
def train(agent: PlayerAgent, game: Union[TrainingGame, PuzzleGame], game_controller: GameController, num_iterations: int) -> None:
    agent.game = game
    agent.controller = game_controller
    agent.mode = PlayerAgent.MODE_EXPLORATION
    lost = 0
    won = 0
    result = 0

    for i in range(num_iterations):
        print(f"Training game {i + 1}")
        game_state = get_state(game)
        while game_state[0] != 'Finish' and game.running:
            _, _, game_state, result = agent.step()

        if result < 0:
            lost += 1
        else:
            won += 1

        agent.controller.execute(GameController.K_ENTER)
    
    print(agent.q)
    print(f"Table size: {len(agent.q)}")
    print(f"Won: {won}")
    print(f"Lost: {lost}")


"""
The agent starts to play the game in explotation mode.
"""
def play(agent: PlayerAgent, game: Union[TrainingGame, PuzzleGame], game_controller: GameController) -> None:
    agent.game = game
    agent.controller = game_controller
    agent.mode = PlayerAgent.MODE_EXPLOTATION
    agent.game_finished = False
    print(f"Playing game")
    game_state = get_state(game)
    while game_state[0] != 'Finish' and game.running:
        _, _, game_state, _ = agent.step()


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
    train(agent, training_game, TrainingGameController(training_game), n)

    game = PuzzleGame(
        title='Puzzle Game',
        window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )
    agent_thread = threading.Thread(target=play, args=(agent, game, GraphicGameController(1.1)))
    agent_thread.start()
    game.exec()
    agent_thread.join()
    