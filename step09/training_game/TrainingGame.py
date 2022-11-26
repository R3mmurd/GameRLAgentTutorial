from typing import Tuple, Optional

from game import settings

class TrainingGame:
    def __init__(self):
        self.init()

    def init(self) -> None:
        self.environment = None
        self.player = None
        self.statue_1 = None
        self.statue_2 = None
        self.target_1 = None
        self.target_2 = None
        self.rows = None
        self.cols = None
        self._load_environment()
        self.state = "Initial"
        self.finish_message = None
        self.running = True
    
    def _load_environment(self) -> None:
        with open(settings.ENVIRONMENT_PATH, 'r') as f:
            rows, cols = f.readline().split(' ')
            self.rows, self.cols = int(rows), int(cols)

            self.environment = [[None for _ in range(self.cols)] for _ in range(self.rows)]
            
            for i in range(self.rows):
                row = f.readline()
                if row[-1] == '\n':
                    row = row[:-1]
                row = row.split(' ')

                for j in range(self.cols):
                    self.environment[i][j] = (row[j] == '0')
                    
            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            self.environment[row][col] = True
            self.player = (row, col)
            
            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            self.environment[row][col] = True
            self.statue_1 = (row, col)

            row, col = f.readline().split(' ')
            row, col = int(row), int(col)
            self.environment[row][col] = True
            self.statue_2 = (row, col)
            
            row, col = f.readline().split(' ')
            self.target_1 = int(row), int(col)

            row, col = f.readline().split(' ')
            self.target_2 = int(row), int(col)

    def move_up_actor(self, actor: str) -> None:
        i, j = getattr(self, actor)
        if i > 0 and not self.environment[i - 1][j]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i - 1, j))
            if actor != 'player':
                self.environment[i - 1][j] = True

    def move_down_actor(self, actor: str) -> None:
        i, j = getattr(self, actor)
        if i < self.rows - 1 and not self.environment[i + 1][j]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i + 1, j))
            if actor != 'player':
                self.environment[i + 1][j] = True
    
    def move_left_actor(self, actor: str) -> None:
        i, j = getattr(self, actor)
        if j > 0 and not self.environment[i][j - 1]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i, j - 1))
            if actor != 'player':
                self.environment[i][j - 1] = True

    def move_right_actor(self, actor: str) -> None:
        i, j = getattr(self, actor)
        if j < self.cols - 1 and not self.environment[i][j + 1]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i, j + 1))
            if actor != 'player':
                self.environment[i][j + 1] = True

    def move_up(self) -> None:
        self.move_up_actor('player')
        self.move_down_actor('statue_1')
        self.move_up_actor('statue_2')
        self.check_lost()
        self.check_win()

    def move_right(self) -> None:
        self.move_right_actor('player')
        self.move_left_actor('statue_1')
        self.move_right_actor('statue_2')
        self.check_lost()
        self.check_win()
    
    def move_down(self) -> None:
        self.move_down_actor('player')
        self.move_up_actor('statue_1')
        self.move_down_actor('statue_2')
        self.check_lost()
        self.check_win()

    def move_left(self) -> None:
        self.move_left_actor('player')
        self.move_right_actor('statue_1')
        self.move_left_actor('statue_2')
        self.check_lost()
        self.check_win()

    def press_enter(self) -> None:
        if self.state == "Initial":
            self.state = "Playing"
        elif self.state == "Finish":
            self.init()

    def get_state_info(self) -> Tuple[str, Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[Tuple[int, int]], Optional[str]]:
        if self.state == "Initial":
            return (self.state, None, None, None, None)
        elif self.state == "Playing":
            return (self.state, self.player, self.statue_1, self.statue_2, None)
        else:
            return (self.state, None, None, None, self.finish_message)
            
    def check_lost(self) -> None:
        if ((self.player == self.statue_1) or
            (self.player == self.statue_2)):
            self.finish_message = 'Lost'
            self.state = "Finish"
    
    def _check_win(self, statue_1: Tuple[int, int], statue_2: Tuple[int, int]) -> bool:
        return self.target_1 == statue_1 and self.target_2 == statue_2

    def check_win(self) -> None:
        if self._check_win(self.statue_1, self.statue_2) or self._check_win(self.statue_2, self.statue_1):
            self.finish_message = "Won"
            self.state = "Finish"
        