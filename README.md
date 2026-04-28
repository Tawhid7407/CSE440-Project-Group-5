# Volcano Grid World MDP - CSE440 AI Project

## 🌋 Project Overview

This is an advanced **Markov Decision Process (MDP)** implementation for navigating a dynamic volcano-themed grid world. An intelligent agent uses **Value Iteration** to compute optimal policies while avoiding hazards (lava, gas, craters) and reaching the goal zone efficiently.

**Group: CSE440-AI Group:5**

---

## 🎯 Objectives

The agent must:
- Navigate from start position **(0, 0)** to goal position **(9, 9)**
- Avoid volcanic hazards: Craters (-100), Lava (-30), and Gas zones (-10)
- Minimize total steps taken (each step costs -1)
- Use MDP Value Iteration to compute optimal policy
- Maximize total reward

---

## 🏗️ Project Structure

```
volcano_mdp/
│
├── main.py                    # Main entry point
├── config.py                  # Configuration & reward definitions
├── requirements.txt           # Python dependencies
├── REWARD_FUNCTION.md         # Reward system documentation
├── README.md                  # This file
│
├── agent/
│   └── explorer.py           # Agent implementation with path navigation
│
├── environment/
│   ├── grid_world.py         # 10x10 grid world environment
│   └── hazards.py            # Dynamic hazard generation
│
├── mdp/
│   └── mdp_solver.py         # MDP Value Iteration solver
│
├── utils/
│   └── visualization.py      # Matplotlib visualization with multiple panels
│
├── blue_bg.png               # Blue background image for visualization
├── ai_bg.png                 # AI-themed background image
├── volcano_bg.png            # Volcano background image (archived)
│
└── __pycache__/              # Python cache (auto-generated)
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Required packages (see Installation)

### Installation

1. **Clone/Navigate to project:**
```bash
cd e:\0.Spring-2026\CSE440-Msrb\Project\volcano_mdp
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the program:**
```bash
python main.py
```

---

## 📋 Features

### 1. **Dynamic Environment**
- 10×10 grid world with randomly placed hazards
- Hazards change every run:
  - 🎯 **Goal**: +100 reward (bottom-right corner)
  - 💥 **Craters**: -100 reward (instant failure)
  - 🔥 **Lava**: -30 reward (close hazard)
  - ☁️ **Gas**: -10 reward (minor hazard)
  - ➡️ **Safe cells**: -1 per step

### 2. **MDP Value Iteration**
- Computes optimal policy for the environment
- Uses discount factor (γ = 0.9)
- Converges to optimal value function
- Handles all hazard locations automatically

### 3. **Intelligent Agent**
- Uses computed optimal policy to navigate
- Step-by-step detailed output showing:
  - Current position
  - Current cell type & reward
  - Best action (↑↓←→)
  - Next position & result
  - Hazard encounters

### 4. **Beautiful Visualization**
Three-panel display with:

**Panel 1: Grid World with Policy**
- Color-coded cells (Green=Goal, Red=Craters, Orange=Lava, Yellow=Gas)
- Policy arrows showing optimal directions
- Agent path animation
- Legend with all hazard types

**Panel 2: Value Function Heatmap**
- Color gradient showing state values
- Numerical values on each cell
- RdYlGn colormap (Red=Low, Green=High)
- Helps understand optimal paths

**Panel 3: Overall Performance Summary**
- Start Position
- Goal Position
- Total Steps (Path Length)
- Reward Breakdown:
  - Goal Reward: +100
  - Step Cost: (steps × -1)
  - Hazard Penalty: (actual hazards encountered)
  - **Total Reward: (dynamic)**
- Mission Status (✅ Completed or ❌ Failed)

### 5. **Interactive Controls**
- 🔄 **Restart Button**: Run another simulation
- ❌ **Exit Button**: Close the program
- Restart loop for multiple runs

---

## 📊 Reward System

| Element | Reward | Description |
|---------|--------|-------------|
| Goal Zone | +100 | Reaching objective |
| Crater | -100 | Robot destroyed |
| Lava Zone | -30 | Close to lava |
| Gas Zone | -10 | Gas cloud |
| Safe Step | -1 | Movement cost |

**Total Reward Calculation:**
```
Total Reward = Goal(+100) + StepCost(steps × -1) + HazardPenalties
```

Example: 18 steps + 1 Lava(-30) + 1 Gas(-10) = 100 - 18 - 30 - 10 = **42**

---

## 🔧 Configuration

Edit `config.py` to customize:

```python
GRID_SIZE = 10              # Grid dimensions (10x10)
GAMMA = 0.9                 # Discount factor
REWARDS = {
    "goal": 100,            # Goal reward
    "crater": -100,         # Crater penalty
    "lava_close": -30,      # Lava penalty
    "gas": -10,             # Gas penalty
    "step": -1              # Movement cost
}
```

---

## 🎮 How to Use

### Run the Program
```bash
python main.py
```

### What Happens
1. **Initialization**: Grid created, hazards randomly placed
2. **MDP Solving**: Value Iteration computes optimal policy (~100ms)
3. **Agent Navigation**: Step-by-step console output showing movement
4. **Completion**: "🎉 OBJECTIVE ACHIEVED!" message
5. **Visualization**: Beautiful 3-panel display opens
6. **Choose Action**: Click Restart or Exit button

### Example Console Output
```
==================================================
                CSE440-AI Group:5                 
==================================================

🤖 Agent Starting at: (0, 0)
============================================================
📋 ROBOT'S REWARD SYSTEM:
  • Objective (Goal):           +100
  • Crater (Robot Destroyed):   -100
  • Lava Zone (Close):           -30
  • Gas Zone:                    -10
  • Each Step (Time Cost):        -1
============================================================

Step 1:
  Position: (0, 0)
  Current Area: 🔥 LAVA (-30)
  🤔 Analyzing... Best Action: DOWN ↓
  ✓ Moved to: (1, 0) | Safe (Movement Cost: -1.0)

[... more steps ...]

Step 18:
  Position: (8, 9)
  Current Area: Safe (Movement Cost: -1.0)
  🤔 Analyzing... Best Action: DOWN ↓
  ✓ Moved to: (9, 9) | 🎯 GOAL (+100)
  🎉 OBJECTIVE ACHIEVED!
```

---

## 📈 Background Images

The project includes multiple themed backgrounds:

- **`blue_bg.png`**: Sky blue gradient with clouds (default)
- **`ai_bg.png`**: Dark tech-themed AI aesthetic
- **`volcano_bg.png`**: Volcanic mountain with lava flows

Switch backgrounds by editing `utils/visualization.py`:
```python
bg_path = 'blue_bg.png'  # Change to desired background
```

---

## 📦 Requirements

All dependencies listed in `requirements.txt`:
```
numpy>=1.19.0
matplotlib>=3.3.0
Pillow>=8.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🧠 Algorithm Explanation

### Value Iteration (MDP Solver)

The MDP Solver computes optimal policies using **Bellman Equation**:

```
V(s) = max(R(s,a) + γ * Σ P(s'|s,a) * V(s'))
```

Where:
- **V(s)**: State value
- **R(s,a)**: Immediate reward for action a in state s
- **γ**: Discount factor (0.9)
- **P(s'|s,a)**: Transition probability
- **π(s)**: Optimal policy (best action in each state)

### Agent Navigation

1. Receives computed optimal policy
2. For each position, looks up best action
3. Takes action and moves to new position
4. Receives reward for that position
5. Continues until goal or out of bounds

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Markov Decision Process fundamentals
- ✅ Value Iteration algorithm
- ✅ Optimal policy computation
- ✅ Dynamic environment adaptation
- ✅ Path planning with constraints
- ✅ Reward system design
- ✅ Interactive visualization
- ✅ Python software engineering best practices

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Program entry point, orchestrates execution flow |
| `config.py` | Global configuration and reward constants |
| `agent/explorer.py` | Agent class with navigation logic |
| `environment/grid_world.py` | 10×10 grid environment |
| `environment/hazards.py` | Dynamic hazard placement |
| `mdp/mdp_solver.py` | Value Iteration implementation |
| `utils/visualization.py` | Matplotlib visualization |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Install requirements: `pip install -r requirements.txt` |
| No visualization | Ensure matplotlib is installed and display is available |
| Background not showing | Check `blue_bg.png` exists in project folder |
| Slow execution | Normal (Value Iteration takes ~100ms per run) |

---

## 🚀 Future Enhancements

Potential improvements:
- [ ] Q-Learning implementation
- [ ] Policy Gradient methods
- [ ] Neural Network-based approximation
- [ ] Real-time policy updates
- [ ] Multi-agent scenarios
- [ ] Larger grid worlds
- [ ] 3D visualization
- [ ] Web-based interface

---

## 👥 Team

**CSE440-AI Group:5**

---

## 📜 License

Educational project - CSE440 AI Course (Spring 2026)

---

## 📞 Support

For questions or issues, refer to:
- `REWARD_FUNCTION.md` - Detailed reward system documentation
- Inline code comments
- Console output for debugging

---

## ✨ Credits

Developed as part of CSE440 Artificial Intelligence course project.

**Project Type**: Markov Decision Process (MDP) Implementation  
**Date**: April 2026  
**Version**: 1.0

---

## 🎉 Enjoy!

Run the project and watch the AI navigate through the volcano!

```bash
python main.py
```

Happy exploring! 🌋✨
