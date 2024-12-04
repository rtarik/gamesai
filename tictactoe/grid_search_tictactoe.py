from tictactoe.env.tictactoe_env import TicTacToeEnv
from algorithms.q_learning_agent import QLearningAgent
from tictactoe.train_tictactoe_qlearning import evaluate_agent
from itertools import product

def grid_search_hyperparameters(
    learning_rates, discount_factors, exploration_decays, min_explorations, episodes=1000, games=100
):
    best_params = None
    best_win_rate = 0
    results = []

    for lr, gamma, decay, min_eps in product(learning_rates, discount_factors, exploration_decays, min_explorations):
        print(f"Testing combination: lr={lr}, gamma={gamma}, decay={decay}, min_eps={min_eps}")
        
        # Initialize environment and agent with current parameters
        env = TicTacToeEnv()
        actions = list(range(9))
        agent = QLearningAgent(
            actions=actions,
            learning_rate=lr,
            discount_factor=gamma,
            exploration_decay=decay,
            min_exploration=min_eps
        )
        
        # Train the agent
        for episode in range(episodes):
            state = env.reset()
            done = False
            while not done:
                action = agent.choose_action(state)
                next_state, reward, done = env.step(action)
                agent.update(state, action, reward, next_state, done)
                state = next_state
        
        # Evaluate the agent
        win_rate, draw_rate = evaluate_agent(agent, games)
        results.append((lr, gamma, decay, min_eps, win_rate, draw_rate))
        
        # Update the best parameters if this combination is better
        if win_rate > best_win_rate:
            best_win_rate = win_rate
            best_params = (lr, gamma, decay, min_eps)
        
        print(f"Win Rate: {win_rate:.2f}% - Best Win Rate So Far: {best_win_rate:.2f}%")

    print("Grid Search Completed!")
    print(f"Best Parameters: lr={best_params[0]}, gamma={best_params[1]}, decay={best_params[2]}, min_eps={best_params[3]}")
    return best_params, results

if __name__ == "__main__":
    # Define hyperparameter ranges
    learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
    discount_factors = [0.9, 0.95, 0.99, 0.995]
    exploration_decays = [0.99, 0.995, 0.999]
    min_explorations = [0.01, 0.05, 0.1]
    
    # Run grid search
    best_params, results = grid_search_hyperparameters(
        learning_rates, discount_factors, exploration_decays, min_explorations, episodes=10000, games=100
    )
    
    # Print all results
    print("\nAll Results:")
    for lr, gamma, decay, min_eps, win_rate, draw_rate in results:
        print(f"lr={lr}, gamma={gamma}, decay={decay}, min_eps={min_eps} -> Win Rate: {win_rate:.2f}%, Draw Rate: {draw_rate:.2f}%")
