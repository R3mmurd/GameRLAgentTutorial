# Game RL Agent Tutorial

Video games, besides being useful as entertainment tools, have the potential to stimulate cognitive skills in people,
such as problems solving. On the other hand, Artificial Intelligence is a branch of Computer Science that looks for designing
agents with the capability to imitate human cognitive skills. In this sense, video games can provide challenging and controlled
environments that allow to test of the performance of traditional agents and stimulate the design of new agents. In this sense,
video games can provide challenging and controlled environments that allow to test of the performance of traditional agents and
stimulate the design of new agents.

This tutorial includes an introduction to video game programming and agents that learn to play them based on the Reinforcement Learning framework.

## The game

The game is a puzzle game based on a challenge taken from The Legend of Zelda: Twilight Princess. Before getting the Master Sword,
the player has to solve a puzzle. There are two statues standing in their original places, then they move to other places, one of 
them at the front of the main character and the other one behind it. The goal is to move the main character up, right, down, or left,
one of the statues will do the same movement and the other one will do it as a mirror, then the player should move around the puzzle
to guide both of the statues to their original positions.

This is a 2D version where the original places of the statues are the sand squares and the cells with plants are cells where the player
and the statues are not able to stand. The logic to solve this puzzle is the mentioned above.

## Development

This tutorial is developed in 9 steps.

1. Game basic infrastructure and empty game states.
2. Building the initial screen.
3. Building the environment from a text file.
4. Entities.
5. Main character and its states.
6. Input handling and animations.
7. Statues and their movements according to the main character's movement.
8. Finish state: Win or Lose.
9. Agent implementation and training game.

## Requirements

### General libraries
- python3-dev
- python3-pip
- python3-venv
- python3-tk

### Libraries from pip
- pygame
- gale
- pyautogui

## Getting started

- Install the general libraries.
- Create a virtual environment and activate it.
- Install the pip libraries with the command `pip install -r requirements.txt`.
- Enter the directory and run `python main.py`. In step 9, the program execution receives as an argument the number of training games for the agent.
  For instance: `python main.py 3500`.

## Authors
- [Alejandro Mujica](http://webdelprofesor.ula.ve/ingenieria/alejandromujica//)
- [Jesús Pérez](http://webdelprofesor.ula.ve/ingenieria/jesuspangulo/)
