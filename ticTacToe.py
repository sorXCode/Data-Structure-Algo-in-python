class TicTacToe:
    """
    TicTacToe game in python using commandline
    """

    def __init__(self):
        """start a new game"""
        self._board = [[' '] * 3 for x in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """Puts mark at loc (i,j) for a player"""
        if (0 <= i <= 2 and 0 <= j <= 2):
            if (self._board[i][j] == ' '):
                self._board[i][j] = self._player
                self._player = 'O' if self._player == 'X' else 'X'
            else:
                raise ValueError("Board Position occupied")
        else:
            raise ValueError("Invalid Board Position")

    def _check_win(self, mark):
        """Checks if a player wins"""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or
                # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or
                # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or
                # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or
                # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or
                # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or
                # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]
                # rev diag
                )

    def winner(self):
        """returns the winner's mark or None if tie"""
        for mark in 'XO':
            if self._check_win(mark):
                return mark
        return None

    def __str__(self):
        """Returns the string representation of the current game board"""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


if __name__ == "__main__":
    game = TicTacToe()

    game.mark(1, 1), game.mark(0, 2)
    game.mark(2, 2), game.mark(0, 0)
    game.mark(0, 1), game.mark(2, 1)
    game.mark(1, 2), game.mark(1, 0)
    game.mark(2, 0)

    print(game)

    winner = game.winner()
    if winner is not None:
        print('Tie')
    else:
        print(winner, 'wins')
