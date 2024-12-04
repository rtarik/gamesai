class TicTacToeEnv:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.done = False
        self.winner = None

    def reset(self):
        """
        Reset the board to the initial state.
        """
        self.board = [' '] * 9
        self.current_player = 'X'
        self.done = False
        self.winner = None
        return self.get_state()

    def get_state(self):
        """
        Return the current board state as a string.
        """
        return ''.join(self.board)

    def get_valid_actions(self):
        """
        Return a list of valid actions (empty cell indices).
        """
        return [i for i, cell in enumerate(self.board) if cell == ' ']
    
    def step(self, action):
        """
        Execute the action and update the board.
        Args:
            action (int): The cell index to place the current player's mark.
            
        Returns:
            state (str): The new board state.
            reward (float): The reward for the current move.
            done (bool): Whether the game is over.
        """
        if self.done:
            return self.get_state(), 0.0, True  # Game already over, no changes.

        # Check if the action is valid
        if self.board[action] != ' ':
            reward = 0.0
            return self.get_state(), 0, False  # Invalid move penalty.

        # Apply the action
        self.board[action] = self.current_player

        # Check for a winner or draw
        if self.check_winner(self.current_player):
            self.done = True
            self.winner = self.current_player
            reward = 100.0 if self.current_player == 'X' else -100.0  # Positive reward for win, negative for loss
        elif ' ' not in self.board:
            self.done = True
            reward = 0.0
        else:
            reward = 0.0  # No result yet

        # Switch to the other player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

        return self.get_state(), reward, self.done



    def check_winner(self, player):
        """
        Check if the given player has won the game.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def render(self):
        """
        Render the board for debugging or text-based interaction.
        """
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()
