import random

class Agent:
    def __init__(self, env, policy):
        self.env = env
        self.policy = policy

    def run(self, start, max_steps=100):
        state = start
        total_reward = 0
        steps = 0
        path = [state]
        visited = set()
        visited.add(state)

        while not self.env.is_terminal(state) and steps < max_steps:
            action = self.policy[state]
            if action is None:
                break

            transitions = self.env.get_transition_states(state, action)

            rand = random.random()
            cumulative = 0
            for next_state, prob in transitions:
                cumulative += prob
                if rand <= cumulative:
                    state = next_state
                    break

            reward = self.env.get_reward(state)
            total_reward += reward

            # Stop if state already visited (prevent infinite loops)
            if state in visited:
                break
            visited.add(state)

            path.append(state)
            steps += 1

        return total_reward, path