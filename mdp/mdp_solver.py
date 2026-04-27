import numpy as np
from config import ACTIONS, GAMMA

class MDPSolver:
    def __init__(self, env):
        self.env = env
        self.V = np.zeros_like(env.grid)
        self.policy = np.zeros(env.grid.shape, dtype=int)

    def get_next_state(self, x, y, action):
        moves = {
            0: (-1, 0),
            1: (1, 0),
            2: (0, -1),
            3: (0, 1)
        }
        dx, dy = moves[action]
        nx, ny = x + dx, y + dy

        if self.env.is_valid(nx, ny):
            return nx, ny
        return x, y

    def value_iteration(self, iterations=100):
        for _ in range(iterations):
            new_V = np.copy(self.V)

            for x in range(self.env.size):
                for y in range(self.env.size):
                    values = []

                    for a in range(len(ACTIONS)):
                        nx, ny = self.get_next_state(x, y, a)
                        reward = self.env.get_cell(nx, ny)
                        values.append(reward + GAMMA * self.V[nx][ny])

                    best_value = max(values)
                    best_action = np.argmax(values)

                    new_V[x][y] = best_value
                    self.policy[x][y] = best_action

            self.V = new_V

        return self.V, self.policy
