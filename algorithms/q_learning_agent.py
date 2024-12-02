import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, exploration_decay=0.995, min_exploration=0.01):
        """
        Q-Learning Agent for reinforcement learning.
        
        Args:
            actions (list): List of all possible actions.
            learning_rate (float): The rate at which the agent learns (α).
            discount_factor (float): The importance of future rewards (γ).
            exploration_rate (float): Probability of exploring (ε).
            exploration_decay (float): Rate at which exploration reduces.
            min_exploration (float): Minimum value for exploration rate.
        """
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.min_exploration = min_exploration
        self.q_table = {}  # Dictionary to hold Q-values

    def get_state_key(self, state):
        """
        Convert the environment state to a tuple to use as a key in Q-table.
        
        Args:
            state (list): The state of the environment.
        
        Returns:
            tuple: A hashable representation of the state.
        """
        return tuple(state)

    def choose_action(self, state):
        """
        Choose an action based on the ε-greedy policy.
        
        Args:
            state (list): The current state of the environment.
        
        Returns:
            int: Chosen action.
        """
        state_key = self.get_state_key(state)
        
        # Exploration
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)
        
        # Exploitation
        if state_key not in self.q_table:
            return random.choice(self.actions)  # Default to random if no Q-value is known
        return max(self.q_table[state_key], key=self.q_table[state_key].get)

    def update(self, state, action, reward, next_state, done):
        """
        Update the Q-value using the Q-learning formula.
        
        Args:
            state (list): Current state.
            action (int): Action taken.
            reward (float): Reward received.
            next_state (list): Next state.
            done (bool): Whether the episode has ended.
        """
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)
        
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0.0 for a in self.actions}
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {a: 0.0 for a in self.actions}
        
        # Q-learning update formula
        best_next_q = max(self.q_table[next_state_key].values())
        td_target = reward + self.discount_factor * best_next_q * (1 - int(done))
        td_error = td_target - self.q_table[state_key][action]
        
        self.q_table[state_key][action] += self.learning_rate * td_error
        
        # Reduce exploration rate
        if done:
            self.exploration_rate = max(self.min_exploration, self.exploration_rate * self.exploration_decay)
