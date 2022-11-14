import settings

class TrainingGame:
    def __init__(self):
        self.init()

    def init(self):
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
    
    def _load_environment(self):
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

    def move_up_actor(self, actor):
        i, j = getattr(self, actor)
        if i > 0 and not self.environment[i - 1][j]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i - 1, j))
            if actor != 'player':
                self.environment[i - 1][j] = True

    def move_down_actor(self, actor):
        i, j = getattr(self, actor)
        if i < self.rows - 1 and not self.environment[i + 1][j]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i + 1, j))
            if actor != 'player':
                self.environment[i + 1][j] = True
    
    def move_left_actor(self, actor):
        i, j = getattr(self, actor)
        if j > 0 and not self.environment[i][j - 1]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i, j - 1))
            if actor != 'player':
                self.environment[i][j - 1] = True

    def move_right_actor(self, actor):
        i, j = getattr(self, actor)
        if j < self.cols - 1 and not self.environment[i][j + 1]:
            if actor != 'player':
                self.environment[i][j] = False
            setattr(self, actor, (i, j + 1))
            if actor != 'player':
                self.environment[i][j + 1] = True

    def move_up(self):
        self.move_up_actor('player')
        self.move_down_actor('statue_1')
        self.move_up_actor('statue_2')
        self.check_lost()
        self.check_win()

    def move_right(self):
        self.move_right_actor('player')
        self.move_left_actor('statue_1')
        self.move_right_actor('statue_2')
        self.check_lost()
        self.check_win()
    
    def move_down(self):
        self.move_down_actor('player')
        self.move_up_actor('statue_1')
        self.move_down_actor('statue_2')
        self.check_lost()
        self.check_win()

    def move_left(self):
        self.move_left_actor('player')
        self.move_right_actor('statue_1')
        self.move_left_actor('statue_2')
        self.check_lost()
        self.check_win()

    def press_enter(self):
        if self.state == "Initial":
            self.state = "Playing"
        elif self.state == "Finish":
            self.init()
            
    def can_go(self, i, j):
        return i >= 0 and j >= 0 and i < self.rows and j < self.cols and not self.environment[i][j]

    def can_move_up(self):
        pi, pj = self.player
        s1i, s1j = self.statue_1
        s2i, s2j = self.statue_2
        return self.can_go(pi - 1, pj) or self.can_go(s1i + 1, s1j) or self.can_go(s2i - 1, s2j)
    
    def can_move_down(self):
        pi, pj = self.player
        s1i, s1j = self.statue_1
        s2i, s2j = self.statue_2
        return self.can_go(pi + 1, pj) or self.can_go(s1i - 1, s1j) or self.can_go(s2i + 1, s2j)
    
    def can_move_right(self):
        pi, pj = self.player
        s1i, s1j = self.statue_1
        s2i, s2j = self.statue_2
        return self.can_go(pi, pj + 1) or self.can_go(s1i, s1j - 1) or self.can_go(s2i, s2j + 1)
    
    def can_move_left(self):
        pi, pj = self.player
        s1i, s1j = self.statue_1
        s2i, s2j = self.statue_2
        return self.can_go(pi, pj - 1) or self.can_go(s1i, s1j + 1) or self.can_go(s2i, s2j - 1)


    def get_state(self):
        if self.state in ("Playing", "Finish"):
            return (self.state, self.player, self.statue_1, self.statue_2, self.target_1, self.target_2)
        else:
            return (self.state, None, None, None, None, None)

    def get_available_actions(self):
        if self.state == "Initial":
            return ('enter',)
        elif self.state == "Playing":
            result = []
            if self.can_move_up():
                result.append('up')
            if self.can_move_down():
                result.append('down')
            if self.can_move_right():
                result.append('right')
            if self.can_move_left():
                result.append('left')
            return tuple(result)
        else:
            return tuple()

    def get_reward(self):
        if self.state in ("Initial", "Playing"):
            return 0
        return 1000 if self.finish_message == 'Won' else -100

    def check_lost(self):
        if ((self.player == self.statue_1) or
            (self.player == self.statue_2)):
            self.finish_message = 'Lost'
            self.state = "Finish"
    
    def _check_win(self, statue_1, statue_2):
        return self.target_1 == statue_1 and self.target_2 == statue_2

    def check_win(self):
        if self._check_win(self.statue_1, self.statue_2) or self._check_win(self.statue_2, self.statue_1):
            self.finish_message = "Won"
            self.state = "Finish"
        