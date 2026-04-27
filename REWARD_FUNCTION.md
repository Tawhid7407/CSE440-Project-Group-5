# 🤖 Reward Function — Robot's "Moral Judgment"

This represents the robot's decision-making system for what actions are good and what are bad.

## Reward Structure

| Situation | Reward | Emoji | Description |
|-----------|--------|-------|-------------|
| **Achieving the objective** | +100 | 🎯 | Robot reaches the goal |
| **Discovering a new area** | +10 | 🗺️ | Exploring unmapped territory |
| **Collecting scientific samples** | +20 | 🧪 | Gathering data |
| **Each step (time cost)** | -1 | ⏱️ | Discourages wasting time |
| **Entering a gas zone** | -10 | ☁️ | Hazardous atmosphere |
| **Moving close to lava** | -30 | 🔥 | Extreme danger zone |
| **Falling into a crater** | -100 | 💥 | Robot destroyed (catastrophic) |

## Configuration

These rewards are defined in `config.py`:

```python
REWARDS = {
    "goal": 100,              # 🎯 Achieving the objective
    "sample_collect": 20,     # 🧪 Collecting samples
    "new_area": 10,           # 🗺️ New discovery
    "step": -1,               # ⏱️ Movement cost
    "gas": -10,               # ☁️ Gas zone
    "lava_close": -30,        # 🔥 Close to lava
    "crater": -100,           # 💥 Robot destroyed
}
```

## How It Works

1. **Value Iteration Algorithm** uses these rewards to compute optimal policies
2. **Discount Factor (γ = 0.9)** balances immediate vs. future rewards
3. **Agent** follows the computed policy to maximize total reward
4. **Console Output** shows step-by-step decisions with reward descriptions
5. **Visualization** displays the value function heatmap (higher = better)

## Agent Decision Making

The robot thinks through each step considering:
- Current location's reward value
- Available actions (UP, DOWN, LEFT, RIGHT)
- Policy arrows show optimal direction
- Seeks high-reward areas while avoiding penalties

---
**Goal**: Navigate to the objective (🎯) while avoiding hazards (🔥💥☁️)
