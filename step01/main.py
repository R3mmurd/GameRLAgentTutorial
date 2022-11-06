import settings

from src.PuzzleGame import PuzzleGame

if __name__ == '__main__':
    game = PuzzleGame(
        title='Puzzle Game',
        window_width=settings.WINDOW_WIDTH,
        window_height=settings.WINDOW_HEIGHT,
        virtual_width=settings.VIRTUAL_WIDTH,
        virtual_height=settings.VIRTUAL_HEIGHT
    )
    game.exec()
