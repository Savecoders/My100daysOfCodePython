from player import Human, Computer

class TicTacToe():

    def __init__(self, size):
        self.size = size
        self.board = [' ' for _ in range(self.size ** 2)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*self.size:(i+1) * self.size] for i in range(self.size)]:
            print(' | '.join(row))

    def print_board_nums(self):
        number_board = [[str(i) for i in range(
            j * self.size, (j+1) * self.size)] for j in range(self.size)]
        for row in number_board:
            print(' | '.join(row))

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square_position, letter):
        if self.board[square_position] == ' ':
            self.board[square_position] = letter
            if self.winner(square_position, letter):
                self.current_winner = letter
            return True
        return False

        """     
    def diagonal(self):
        arr, arr2, arr3 = [],[],[]
        container1 = 0
        container2 = self.size - 1
        cont = [i for i, _ in enumerate(self.board)]
        
        # the direccion is: \
        for i in cont:
            if i == container1:
                arr.append(self.board[i])
                container1 += self.size + 1
        # the direccion is: /
        for i in cont:
            if i == container2:
                arr2.append(self.board[i])
                container2 += (self.size -1)

        return [arr, arr2] 
        """

    def winner(self, square_position, letter):

        # check row
        row_ind = square_position // self.size
        row = self.board[row_ind * self.size: (row_ind + 1) * self.size]

        if all(spot == letter for spot in row):
            return True

        # check column
        col_ind = square_position % self.size
        column = [self.board[col_ind + i * self.size]
                  for i in range(self.size)]

        if all(spot == letter for spot in column):
            return True

        #isPair = self.size % 2 == 0

        if square_position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True

        """ if isPair == False:
            if square_position % 2 == 0:
                diagonal1 = [self.board[i] for i in self.diagonal()[0]]
                if all([spot == letter for spot in diagonal1]):
                    return True
                diagonal2 = [self.board[i] for i in self.diagonal()[1]]
                if all([spot == letter for spot in diagonal2]):
                    return True
        else:
            if not (square_position % 2 == 0):
                diagonal1 = [self.board[i] for i in self.diagonal()[0]]
                if all([spot == letter for spot in diagonal1]):
                    return True
                diagonal2 = [self.board[i] for i in self.diagonal()[1]]
                if all([spot == letter for spot in diagonal2]):
                    return True """

        # if all fake
        return False


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'Makes a move to square {square} ')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print('It\'s a tie!')

if __name__ == '__main__':
    x_player = Human('X')
    o_player = Computer('O')
    tictactoe = TicTacToe(3)
    play(tictactoe, x_player, o_player, print_game=True)
