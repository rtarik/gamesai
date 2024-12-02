from tictactoe.env.tictactoe_env import TicTacToeEnv
from algorithms.q_learning_agent import QLearningAgent
import numpy as np
import random

def train_agent(episodes=1000):
    # Initialize environment and agent
    env = TicTacToeEnv()
    actions = list(range(9))  # Tic Tac Toe has 9 possible actions
    agent = QLearningAgent(actions)

    # Training loop
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            total_reward += reward
            state = next_state

        # Print progress every 100 episodes
        if (episode + 1) % 100 == 0:
            print(f"Episode {episode + 1}/{episodes} - Total Reward: {total_reward}")

    print("Training completed!")
    return agent

def evaluate_agent(agent, games=100):
    """
    Evaluate the trained agent by playing games against a random opponent.
    
    Args:
        agent (QLearningAgent): The trained Q-learning agent.
        games (int): Number of games to evaluate.
    
    Returns:
        win_rate (float): Percentage of games won by the agent.
        draw_rate (float): Percentage of games ending in a draw.
    """
    env = TicTacToeEnv()
    agent_wins = 0
    draws = 0

    for _ in range(games):
        state = env.reset()
        done = False

        while not done:
            # Agent's turn
            if env.current_player == 'X':
                action = agent.choose_action(state)
            else:  # Random opponent's turn
                valid_actions = [i for i, cell in enumerate(state) if cell == ' ']
                action = random.choice(valid_actions)

            state, _, done = env.step(action)

        # Check the result
        if env.winner == 'X':
            agent_wins += 1
        elif env.winner is None:
            draws += 1

    win_rate = (agent_wins / games) * 100
    draw_rate = (draws / games) * 100
    print(f"Evaluation Results: {games} games")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Draw Rate: {draw_rate:.2f}%")
    print(f"Loss Rate: {100 - win_rate - draw_rate:.2f}%")
    return win_rate, draw_rate

if __name__ == "__main__":
    # Train the agent
    trained_agent = train_agent(episodes=1000)
    
    # Evaluate the trained agent
    evaluate_agent(trained_agent, games=100)
