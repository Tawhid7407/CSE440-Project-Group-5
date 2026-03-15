from environment import VolcanoEnvironment
from mdp_solver import ValueIteration
from agent import Agent
from visualization import print_grid

grid = [
    [0,0,0,1,0,0],
    [0,3,0,0,2,0],
    [0,0,0,1,0,0],
    [0,2,0,0,0,4],
    [0,0,3,0,0,0],
    [0,0,0,0,0,5]
]

env = VolcanoEnvironment(grid)

solver = ValueIteration(env)
solver.run()

agent = Agent(env, solver.policy)

reward, path = agent.run((0,0))

print("Total Reward:", reward)
print("Path:", path)
print_grid(grid, path)