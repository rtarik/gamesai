from tictactoe.env.tictactoe_env import TicTacToeEnv
from algorithms.q_learning_agent import QLearningAgent
import random

def self_play_train_agent(episodes=1000):
    # Initialize environment and agents
    env = TicTacToeEnv()
    actions = list(range(9))  # Tic Tac Toe has 9 possible actions
    agent_X = QLearningAgent(actions, learning_rate=0.0001, exploration_decay=0.95, min_exploration=0.01)
    agent_O = QLearningAgent(actions, learning_rate=0.005, exploration_decay=0.995, min_exploration=0.01)

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            if env.current_player == 'X':
                # Player X chooses action
                action = agent_X.choose_action(state)
            else:
                # Player O chooses action
                action = agent_O.choose_action(state)
            
            next_state, reward, done = env.step(action)
            agent_X.update(state, action, reward, next_state, done)
            agent_O.update(state, action, -reward, next_state, done)
            state = next_state

        # Print progress every 100 episodes
        if (episode + 1) % 100 == 0:
            print(f"Episode {episode + 1}/{episodes} - Reward X: {reward}, Reward O: {-reward}")

    print("Self-play training completed!")
    return agent_X, agent_O

def evaluate_agent(agent, games=100, player='X'):
    """
    Evaluate a trained agent by playing games against a random opponent.
    Args:
        agent (QLearningAgent): The trained Q-learning agent.
        games (int): Number of games to evaluate.
        player (str): 'X' or 'O', the side the agent plays.
    """
    env = TicTacToeEnv()
    agent_wins = 0
    draws = 0

    for _ in range(games):
        state = env.reset()
        done = False

        while not done:
            if env.current_player == player:
                # Agent's turn
                action = agent.choose_action(state)
            else:
                # Random opponent's turn
                valid_actions = env.get_valid_actions()
                action = random.choice(valid_actions)

            state, _, done = env.step(action)

        # Check the result
        if env.winner == player:
            agent_wins += 1
        elif env.winner is None:
            draws += 1

    win_rate = (agent_wins / games) * 100
    draw_rate = (draws / games) * 100
    loss_rate = 100 - win_rate - draw_rate
    print(f"Evaluation Results for {player}: {games} games")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Draw Rate: {draw_rate:.2f}%")
    print(f"Loss Rate: {loss_rate:.2f}%")
    return win_rate, draw_rate, loss_rate

if __name__ == "__main__":
    # Train the agents via self-play
    agent_X, agent_O = self_play_train_agent(episodes=1000)

    # Evaluate both agents
    print("\nEvaluating Agent X:")
    evaluate_agent(agent_X, games=100, player='X')

    print("\nEvaluating Agent O:")
    evaluate_agent(agent_O, games=100, player='O')
