class TicTacToe:
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    players = ['X', 'O']

    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def print_board(self):
        for row in self.board:
            for cell in row:
                print('| {} |'.format(cell), end='')
            print('\n')

    def step(self, index):
        self.print_board()
        print('Ход делают - {}'.format(TicTacToe.players[index]))
        step_cell = int(input('В какую клетку делаем шаг? '))
        for row in self.board:
            for i in range(len(row)):
                if row[i] == step_cell:
                    row[i] = TicTacToe.players[index]
        calc_dict = self.calc_cell()
        if self.check_win(calc_dict['x']):
            print('Победили крестики!')
        elif self.check_win(calc_dict['o']):
            print('Победили нолики!')
        elif self.check_free_cell(calc_dict['free']):
            print('Ничья!')
        else:
            return True
        self.print_board()
        return False

    def calc_cell(self):
        x_check = []
        o_check = []
        free_cell = []
        for row in range(len(self.board)):
            for cell in range(len(self.board[row])):
                if self.board[row][cell] == TicTacToe.players[0]:
                    x_check.append(row * 3 + cell + 1)
                if self.board[row][cell] == TicTacToe.players[1]:
                    o_check.append(row * 3 + cell + 1)
                if self.board[row][cell] in range (1, 10):
                    free_cell.append(row * 3 + cell + 1)
        cells_dict = {'x': x_check, 'o': o_check, 'free': free_cell}
        return cells_dict

    def check_win(self, cells):
        for comb in TicTacToe.wins:
            count = 0
            for i in comb:
                if i in cells:
                    count += 1
            if count == 3:
                return True
        return False

    def check_free_cell(self, cells):
        if len(cells) == 0:
            return True
        else:
            return False

tic = TicTacToe()
step = 0
while True:
    if tic.step(step%2):
        step += 1
    else:
        break