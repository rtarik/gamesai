import numpy as np

class TicTacToeEnv:
    def __init__(self):
        """
        Initialize the Tic Tac Toe environment.
        """
        self.state = np.zeros(9, dtype=int)  # 1D array representing the board
        self.done = False  # Whether the game has ended
        self.current_player = 1  # 1 for Player 1, -1 for Player 2

    def reset(self):
        """
        Reset the environment to the initial state.
        :return: The initial state of the board.
        """
        self.state = np.zeros(9, dtype=int)
        self.done = False
        self.current_player = 1
        return self.state

    def step(self, action):
        """
        Take a step in the environment by making a move.
        :param action: The index (0-8) of the cell to play.
        :return: Tuple (state, reward, done)
        """
        if self.done:
            raise ValueError("Game has ended. Please reset the environment.")
        if self.state[action] != 0:
            return self.state, -1, True  # Invalid move: return penalty and end game
        
        # Make the move
        self.state[action] = self.current_player

        # Check for a winner or draw
        reward, self.done = self.check_game_status()
        
        # Switch player if the game isn't done
        if not self.done:
            self.current_player *= -1
        
        return self.state, reward, self.done

    def check_game_status(self):
        """
        Check the game status to determine if someone has won or if there's a draw.
        :return: Tuple (reward, done)
        """
        # Winning combinations
        win_states = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for line in win_states:
            if abs(self.state[line].sum()) == 3:
                return (1 if self.state[line[0]] == self.current_player else -1), True
        
        # Check for a draw
        if 0 not in self.state:
            return 0, True
        
        return 0, False  # Game continues

    def render(self):
        """
        Render the current state of the board.
        """
        symbols = {0: ".", 1: "X", -1: "O"}
        board = [symbols[cell] for cell in self.state]
        print("\n".join([" ".join(board[i:i+3]) for i in range(0, 9, 3)]))
