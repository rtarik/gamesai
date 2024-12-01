import unittest
from tictactoe.env.tictactoe_env import TicTacToeEnv

class TestTicTacToeEnv(unittest.TestCase):

    def setUp(self):
        """
        Set up a new TicTacToeEnv instance before each test.
        """
        self.env = TicTacToeEnv()

    def test_initial_state(self):
        """
        Test that the initial state of the board is empty.
        """
        self.assertEqual(self.env.board, [' '] * 9)
        self.assertEqual(self.env.current_player, 'X')

    def test_valid_action(self):
        """
        Test that a valid action (like placing 'X' or 'O') updates the board correctly.
        """
        self.env.step(0)  # Player 'X' makes a move in the top-left corner
        self.assertEqual(self.env.board[0], 'X')

    def test_invalid_action(self):
        """
        Test that an invalid action (like placing a move in an already occupied cell)
        does not change the board and returns the appropriate message.
        """
        self.env.step(0)  # Player 'X' makes a move in the top-left corner
        result = self.env.step(0)  # Player 'O' tries to place a move in the same position
    
        # The board should remain unchanged
        self.assertEqual(self.env.board[0], 'X')
    
        # Result should indicate an invalid move, no change in board, and game not over
        self.assertEqual(result, (self.env.get_state(), -0.1, False))


    def test_winning_condition(self):
        """
        Test the winning condition when a player wins.
        """
        # Simulate a winning move for player 'X'
        self.env.step(0)  # 'X' in top-left
        self.env.step(1)  # 'O' in top-center
        self.env.step(3)  # 'X' in middle-left
        self.env.step(4)  # 'O' in center
        self.env.step(6)  # 'X' in bottom-left (winning move)
        
        self.assertTrue(self.env.done)
        self.assertEqual(self.env.winner, 'X')

def test_draw_condition(self):
    """
    Test the draw condition when all cells are filled and no player wins.
    """
    # Simulate a draw situation (no winner and the board is full)
    self.env.step(0)  # 'X'
    self.env.step(1)  # 'O'
    self.env.step(2)  # 'X'
    self.env.step(4)  # 'O'
    self.env.step(3)  # 'X'
    self.env.step(5)  # 'O'
    self.env.step(7)  # 'X'
    self.env.step(6)  # 'O'
    result = self.env.step(8)  # 'X' completes the draw

    # Assert that the game is marked as done
    self.assertTrue(self.env.done)
    # Assert that there is no winner (it's a draw)
    self.assertEqual(self.env.winner, None)
    # Assert that the game correctly announces a draw
    self.assertEqual(result[0], 'Game Over! It\'s a draw.')

    def test_reset(self):
        """
        Test the reset functionality of the environment.
        """
        self.env.step(0)  # Make a move
        self.env.reset()  # Reset the environment
        self.assertEqual(self.env.board, [' '] * 9)  # The board should be empty
        self.assertEqual(self.env.current_player, 'X')  # It's 'X' turn again after reset

if __name__ == "__main__":
    unittest.main()
