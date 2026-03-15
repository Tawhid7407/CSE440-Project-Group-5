class ValueIteration:
    def __init__(self, env, theta=0.001):
        self.env = env
        self.theta = theta
        self.V = {state: 0 for state in env.get_states()}
        self.policy = {}

    def run(self):
        while True:
            delta = 0
            for state in self.env.get_states():
                if self.env.is_terminal(state):
                    continue

                v = self.V[state]
                action_values = []

                for action in self.env.actions:
                    total = 0
                    for next_state, prob in self.env.get_transition_states(state, action):
                        reward = self.env.get_reward(next_state)
                        total += prob * (reward + self.env.gamma * self.V[next_state])
                    action_values.append(total)

                self.V[state] = max(action_values)
                delta = max(delta, abs(v - self.V[state]))

            if delta < self.theta:
                break

        self.extract_policy()

    def extract_policy(self):
        for state in self.env.get_states():
            if self.env.is_terminal(state):
                self.policy[state] = None
                continue

            best_action = None
            best_value = float('-inf')

            for action in self.env.actions:
                total = 0
                for next_state, prob in self.env.get_transition_states(state, action):
                    reward = self.env.get_reward(next_state)
                    total += prob * (reward + self.env.gamma * self.V[next_state])

                if total > best_value:
                    best_value = total
                    best_action = action

            self.policy[state] = best_action