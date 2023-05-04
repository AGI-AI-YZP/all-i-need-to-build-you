import gym
import numpy as np

# Create the CartPole environment
env = gym.make('CartPole-v1')

# Initialize the Q-table to zero
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Set the hyperparameters
alpha = 0.5
gamma = 0.95
epsilon = 0.1
episodes = 50000

# For each episode
for episode in range(episodes):
    # Reset the state
    state = env.reset()

    done = False
    while not done:
        # Choose an action
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state, :])  # Exploit

        # Perform the action
        next_state, reward, done, info = env.step(action)

        # Update the Q-table
        Q[state, action] = (1 - alpha) * Q[state, action] + \
            alpha * (reward + gamma * np.max(Q[next_state, :]))

        # Update the current state
        state = next_state

# Print the optimal policy
print(np.argmax(Q, axis=1))

# Print the optimal Q-values
print(np.max(Q, axis=1))
