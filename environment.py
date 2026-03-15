import numpy as np
import random

class VolcanoEnvironment:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.rows, self.cols = self.grid.shape
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.gamma = 0.9  # Discount factor

    def get_states(self):
        return [(r, c) for r in range(self.rows) for c in range(self.cols)]

    def is_terminal(self, state):
        r, c = state
        return self.grid[r][c] in [1, 3, 5]  # Lava, Crater, Goal

    def get_reward(self, state):
        r, c = state
        cell = self.grid[r][c]
        if cell == 0:   # Safe move
            return -1
        elif cell == 1: # Lava
            return -100
        elif cell == 2: # Gas
            return -50
        elif cell == 3: # Crater
            return -200
        elif cell == 4: # Data Station
            return 50
        elif cell == 5: # Goal
            return 200

    def move(self, state, action):
        r, c = state
        if action == "UP":
            r = max(r - 1, 0)
        elif action == "DOWN":
            r = min(r + 1, self.rows - 1)
        elif action == "LEFT":
            c = max(c - 1, 0)
        elif action == "RIGHT":
            c = min(c + 1, self.cols - 1)
        return (r, c)

    def get_transition_states(self, state, action):
        # 80% intended, 10% slip each side
        probs = []
        intended = self.move(state, action)

        if action in ["UP", "DOWN"]:
            slip1 = self.move(state, "LEFT")
            slip2 = self.move(state, "RIGHT")
        else:
            slip1 = self.move(state, "UP")
            slip2 = self.move(state, "DOWN")

        probs.append((intended, 0.8))
        probs.append((slip1, 0.1))
        probs.append((slip2, 0.1))
        return probs