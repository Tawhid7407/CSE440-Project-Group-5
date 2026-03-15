# Volcano MDP

A simple Markov Decision Process (MDP) solver for navigating a grid-based volcano environment.

The project uses **value iteration** to compute an optimal policy and then runs a simulated agent to follow the policy.

---

## 🧠 Environment

The grid is represented as a 2D array where each cell type has a reward/penalty:

- `0` – Safe cell (reward: -1)
- `1` – Lava (reward: -100)
- `2` – Gas (reward: -50)
- `3` – Crater (reward: -200)
- `4` – Data Station (reward: +50)
- `5` – Goal (reward: +200)

The agent can move in 4 directions: `UP`, `DOWN`, `LEFT`, `RIGHT`. Moves are stochastic (80% intended direction, 10% slip left/right).

---

## ▶️ Run

### Requirements

- Python 3.8+

### Run the demo

From the project directory:

```bash
python main.py
```

This will:

1. Build the environment (in `main.py`)
2. Run value iteration (`mdp_solver.py`)
3. Simulate the agent following the policy (`agent.py`)
4. Print the total reward, path, and a grid view with the agent path

---

## 📁 Project structure

- `main.py` – entry point (defines the grid and runs everything)
- `environment.py` – defines the MDP environment / transitions / rewards
- `mdp_solver.py` – value iteration solver + policy extraction
- `agent.py` – policy execution with stochastic transitions
- `visualization.py` – simple terminal visualization of the path

---

## ✏️ Customize

To try a different grid, edit the `grid` variable in `main.py`.

---

## 📌 Notes

This project is intended as a small educational demo of MDPs and value iteration, and is not intended for production use.
