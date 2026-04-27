GRID_SIZE = 10

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

GAMMA = 0.9   # discount factor

# Reward Function — Robot's "Moral Judgment"
REWARDS = {
    "new_area": 10,              # Discovering a new area
    "sample_collect": 20,        # Collecting scientific samples
    "goal": 100,                 # Achieving the objective
    "step": -1,                  # Each step (discourage wasting time)
    "gas": -10,                  # Entering a gas zone
    "lava_close": -30,           # Moving close to lava
    "crater": -100,              # Falling into a crater (robot destroyed)
    "safe": -1                   # Moving through safe area
}

# Reward Matrix for visualization
REWARD_DESCRIPTIONS = {
    "goal": ("🎯 Objective", 100, "Goal"),
    "crater": ("💥 Crater", -100, "Robot Destroyed"),
    "lava_close": ("🔥 Lava", -30, "Close to Lava"),
    "gas": ("☁️ Gas", -10, "Gas Zone"),
    "step": ("➡️ Step", -1, "Movement Cost"),
}
