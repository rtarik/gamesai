import unittest
from env.tictactoe_env import TicTacToeEnv

class TestTicTacToeEnv(unittest.TestCase):
    def setUp(self):
        self.env = TicTacToeEnv()

    def test_reset(self):
        state = self.env.reset()
        self.assertTrue((state == 0).all())
        self.assertFalse(self.env.done)

    def test_valid_move(self):
        self.env.reset()
        state, reward, done = self.env.step(0)
        self.assertEqual(state[0], 1)
        self.assertEqual(reward, 0)
        self.assertFalse(done)

    def test_invalid_move(self):
        self.env.reset()
        self.env.step(0)
        _, reward, done = self.env.step(0)
        self.assertEqual(reward, -1)
        self.assertTrue(done)

    def test_win_condition(self):
        self.env.reset()
        self.env.step(0)  # X
        self.env.step(3)  # O
        self.env.step(1)  # X
        self.env.step(4)  # O
        _, reward, done = self.env.step(2)  # X wins
        self.assertEqual(reward, 1)
        self.assertTrue(done)

    def test_draw_condition(self):
        self.env.reset()
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
        for i, move in enumerate(moves):
            _, reward, done = self.env.step(move)
            if i < 8:
                self.assertFalse(done)
            else:
                self.assertTrue(done)
                self.assertEqual(reward, 0)

if __name__ == "__main__":
    unittest.main()
