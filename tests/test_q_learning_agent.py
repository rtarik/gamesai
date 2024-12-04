import unittest
from algorithms.q_learning_agent import QLearningAgent
import numpy as np

class TestQLearningAgent(unittest.TestCase):
    def setUp(self):
        self.actions = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Tic Tac Toe actions
        self.agent = QLearningAgent(self.actions)

    def test_initialization(self):
        self.assertEqual(len(self.agent.q_table), 0, "Q-table should be empty upon initialization.")

    def test_choose_action_exploitation(self):
        # Mock Q-table with high-value actions
        state = 'test_state'
        state_key = self.agent.get_state_key(state)
        self.agent.q_table[state_key] = {a: 1.0 if a == 4 else 0.5 for a in self.actions}
        self.agent.exploration_rate = 0  # Force exploitation
        action = self.agent.choose_action(state)
        self.assertEqual(action, 4, "Agent should exploit and choose the action with the highest Q-value.")

    def test_choose_action_exploration(self):
        state = 'test_state'
        state_key = self.agent.get_state_key(state)
        self.agent.q_table[state_key] = {a: 1.0 for a in self.actions}
        self.agent.epsilon = 1  # Force exploration
        action = self.agent.choose_action(state)
        self.assertIn(action, self.actions, "Agent should explore and choose any valid action.")

    def test_q_table_update(self):
        """
        Test that the Q-value table is updated correctly.
        """
        # Initialize the agent with possible actions 0-8 for Tic Tac Toe
        agent = QLearningAgent(actions=list(range(9)), learning_rate=0.1, discount_factor=0.95, exploration_rate=0.1)
        
        # Set up initial state-action values for the test
        state = 'state1'
        action = 0
        next_state = 'state2'
        state_key = agent.get_state_key(state)
        next_state_key = agent.get_state_key(next_state)
        reward = 1.0
        done = False  # The episode is not finished in this test

        # Initialize Q-values for the states
        agent.q_table[state_key] = {a: 0.5 for a in agent.actions}  # Q-values for the current state
        agent.q_table[next_state_key] = {a: 0.8 for a in agent.actions}  # Q-values for the next state

        # Perform the update
        agent.update(state, action, reward, next_state, done)

        # Calculate expected Q-value
        current_q = 0.5
        max_next_q = 0.8
        learning_rate = 0.1
        discount_factor = 0.95
        expected_q = current_q + learning_rate * (reward + discount_factor * max_next_q - current_q)

        # Check the updated Q-value
        updated_q = agent.q_table[state_key][action]
        self.assertAlmostEqual(updated_q, expected_q, places=5, msg="Q-value update is incorrect.")


if __name__ == "__main__":
    unittest.main()
