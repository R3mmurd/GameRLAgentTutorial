import sys
import threading

from game import settings

from adapters import GameController, GraphicGameController, TrainingGameController
from training_game.TrainingGame import TrainingGame

from game.src.PuzzleGame import PuzzleGame
from AI.PlayerAgent import PlayerAgent

def get_state(game):
    return game.get_state_info()

def get_available_actions(game):
    state_name, _, _, _, _ = game.get_state_info()
    if state_name == "Initial":
        return (GameController.K_ENTER,)
    elif state_name == "Playing":
        return (GameController.K_UP, GameController.K_RIGHT, GameController.K_DOWN, GameController.K_LEFT)
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

def get_new_game():
    return PuzzleGame(
        title='Puzzle Game',
        window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )


def train(agent, game, game_controller, num_iterations):
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

def play(agent, game, game_controller):
    agent.game = game
    agent.controller = game_controller
    agent.mode = PlayerAgent.MODE_EXPLOTATION
    agent.game_finished = False
    print(f"Playing game")
    game_state = get_state(game)
    while game_state[0] != 'Finish' and game.running:
        _, _, game_state, _ = agent.step()
        
def start_agent_play_game(agent, game, game_controller):
    play(agent, game, game_controller)

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

    game = get_new_game()
    agent_thread = threading.Thread(target=start_agent_play_game, args=(agent, game, GraphicGameController(1.1)))
    agent_thread.start()
    game.exec()
    agent_thread.join()
    