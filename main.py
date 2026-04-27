from environment.grid_world import GridWorld
from environment.hazards import generate_dynamic_hazards
from mdp.mdp_solver import MDPSolver
from agent.explorer import Explorer
from utils.visualization import plot_grid

def main():
    while True:
        # Create environment with dynamic hazards
        env = GridWorld()
        generate_dynamic_hazards(env)

        # Solve MDP
        solver = MDPSolver(env)
        V, policy = solver.value_iteration()

        # Run agent with dynamic hazards
        agent = Explorer(env, policy)
        path = agent.run()

        # Visualization with policy arrows and value heatmap
        # Returns 'yes' to restart, 'no' to exit
        choice = plot_grid(env, path, animate=True, value_func=V, policy=policy)
        
        if choice == 'yes':
            print("\n" + "="*50)
            continue
        else:
            print("✅ Thank you for running! Goodbye!")
            break

if __name__ == "__main__":
    main()
