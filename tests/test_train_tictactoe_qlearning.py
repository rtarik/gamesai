import unittest
from tictactoe.train_tictactoe_qlearning import train_agent, evaluate_agent
from tictactoe.env.tictactoe_env import TicTacToeEnv
from algorithms.q_learning_agent import QLearningAgent

class TestTrainTicTacToeQLearning(unittest.TestCase):
    def test_train_agent(self):
        agent = train_agent(episodes=10)
        self.assertIsInstance(agent, QLearningAgent, "train_agent should return a QLearningAgent instance.")
        self.assertGreater(len(agent.q_table), 0, "Q-table should not be empty after training.")

    def test_evaluate_agent(self):
        env = TicTacToeEnv()
        actions = list(range(9))
        agent = QLearningAgent(actions)

        # Simulate a trained agent (basic Q-table setup)
        agent.q_table['dummy_state'] = {a: 0.5 for a in actions}

        win_rate, draw_rate = evaluate_agent(agent, games=10)
        self.assertGreaterEqual(win_rate, 0, "Win rate should be non-negative.")
        self.assertLessEqual(win_rate, 100, "Win rate should not exceed 100%.")
        self.assertGreaterEqual(draw_rate, 0, "Draw rate should be non-negative.")
        self.assertLessEqual(draw_rate, 100, "Draw rate should not exceed 100%.")

if __name__ == "__main__":
    unittest.main()
