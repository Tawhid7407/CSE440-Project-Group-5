import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.patches import Patch
from matplotlib.widgets import Button
from config import REWARDS
from PIL import Image
import os



def plot_grid(env, path=None, animate=False, value_func=None, policy=None):
    """Enhanced visualization with policy arrows and value heatmap"""
    grid = env.grid
    fig = plt.figure(figsize=(18, 7))


    
    # Add blue background if available
    bg_path = 'blue_bg.png'
    if os.path.exists(bg_path):
        try:
            bg_img = Image.open(bg_path)
            # Set background using the image
            bg_array = np.array(bg_img)
            fig.set_facecolor('#87CEEB')  # Sky blue background
        except Exception as e:
            print(f"Note: Could not load background image: {e}")
            fig.set_facecolor('#87CEEB')
    else:
        fig.set_facecolor('#87CEEB')


    
    # Add group title
    fig.suptitle('CSE440-AI Group:5', fontsize=16, fontweight='bold', y=0.98, color='darkblue')
    
    # Main grid visualization
    ax1 = plt.subplot(1, 3, 1)
    ax = ax1



    # Create colored grid based on cell values
    colored_grid = np.zeros((env.size, env.size, 3))
    
    for i in range(env.size):
        for j in range(env.size):
            val = grid[i][j]
            if val == REWARDS["goal"]:
                colored_grid[i, j] = [0, 1, 0]  # Green - Goal (+100)
            elif val == REWARDS["crater"]:
                colored_grid[i, j] = [1, 0, 0]  # Red - Crater (-100)
            elif val == REWARDS["lava_close"]:
                colored_grid[i, j] = [1, 0.5, 0]  # Orange - Lava (-30)
            elif val == REWARDS["gas"]:
                colored_grid[i, j] = [1, 1, 0]  # Yellow - Gas (-10)
            else:
                colored_grid[i, j] = [0.9, 0.9, 0.9]  # Light Gray - Safe (-1)

    im = ax.imshow(colored_grid)



    
    # Labels on grid cells
    for i in range(env.size):
        for j in range(env.size):
            val = grid[i][j]
            if val == REWARDS["goal"]:
                ax.text(j, i, '🎯', ha='center', va='center', fontsize=12, fontweight='bold')
            elif val == REWARDS["crater"]:
                ax.text(j, i, '💥', ha='center', va='center', fontsize=12, fontweight='bold')
            elif val == REWARDS["lava_close"]:
                ax.text(j, i, '🔥', ha='center', va='center', fontsize=12, fontweight='bold')
            elif val == REWARDS["gas"]:
                ax.text(j, i, '☁️', ha='center', va='center', fontsize=10, fontweight='bold')


    
    # Add legend
    legend_elements = [
        Patch(facecolor=[0, 1, 0], label=f'🎯 Goal - +{REWARDS["goal"]}'),
        Patch(facecolor=[1, 0, 0], label=f'💥 Crater - {REWARDS["crater"]}'),
        Patch(facecolor=[1, 0.5, 0], label=f'🔥 Lava - {REWARDS["lava_close"]}'),
        Patch(facecolor=[1, 1, 0], label=f'☁️ Gas - {REWARDS["gas"]}'),
        Patch(facecolor=[0.9, 0.9, 0.9], label=f'Safe Step - {REWARDS["step"]}'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=9)


    
    # Add policy arrows
    if policy is not None:
        arrow_labels = {0: '↑', 1: '↓', 2: '←', 3: '→'}
        
        for i in range(env.size):
            for j in range(env.size):
                val = grid[i][j]
                # Only show arrows on safe cells
                if val not in [REWARDS["goal"], REWARDS["crater"], REWARDS["lava_close"], REWARDS["gas"]]:
                    action = policy[i][j]
                    ax.text(j, i, arrow_labels[action], ha='center', va='center', 
                            fontsize=14, fontweight='bold', color='blue', alpha=0.6)

    ax.set_title('Grid World MDP - Policy with Arrows', fontsize=12, fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')



    
    # Value heatmap visualization
    if value_func is not None:
        ax2 = plt.subplot(1, 3, 2)
        
        # Create heatmap of values
        heatmap = np.copy(value_func)
        heatmap_display = np.clip(heatmap, -100, 100)
        
        im = ax2.imshow(heatmap_display, cmap='RdYlGn', interpolation='nearest')
        
        # Add value text on heatmap
        for i in range(env.size):
            for j in range(env.size):
                text = ax2.text(j, i, f'{heatmap[i, j]:.1f}', 
                               ha="center", va="center", color="black", fontsize=7)
        
        ax2.set_title('Value Function Heatmap', fontsize=12, fontweight='bold')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        cbar = plt.colorbar(im, ax=ax2)
        cbar.set_label('Value')


    
    # Performance Summary Panel
    if path is not None:
        ax3 = plt.subplot(1, 3, 3)
        ax3.axis('off')
        
        # Extract path information
        start_pos = path[0]
        end_pos = path[-1]
        total_steps = len(path) - 1
        
        # Check if goal was reached
        end_cell_value = env.get_cell(end_pos[0], end_pos[1])
        mission_status = "✅ Completed" if end_cell_value == REWARDS["goal"] else "❌ Failed"
        
        # Calculate total reward including all hazards and penalties
        total_reward = 0
        step_costs = total_steps * REWARDS["step"]  # -1 per step
        hazard_penalties = 0



        
        # Sum rewards/penalties for all cells in the path
        for x, y in path:
            cell_val = env.get_cell(x, y)
            if cell_val == REWARDS["goal"]:
                total_reward += REWARDS["goal"]
            elif cell_val == REWARDS["crater"]:
                total_reward += REWARDS["crater"]
            elif cell_val == REWARDS["lava_close"]:
                hazard_penalties += REWARDS["lava_close"]
                total_reward += REWARDS["lava_close"]
            elif cell_val == REWARDS["gas"]:
                hazard_penalties += REWARDS["gas"]
                total_reward += REWARDS["gas"]
            else:
                total_reward += REWARDS["step"]
        
        # Find goal position on grid
        goal_pos = None
        for i in range(env.size):
            for j in range(env.size):
                if env.get_cell(i, j) == REWARDS["goal"]:
                    goal_pos = (i, j)
                    break
        
        # Create performance summary text with detailed reward breakdown
        summary_text = f"""




        
📊 OVERALL PERFORMANCE

Start Position:
   ({start_pos[0]}, {start_pos[1]})

Goal Position:
   {f"({goal_pos[0]}, {goal_pos[1]})" if goal_pos else "Unknown"}

Total Steps (Path Length):
   {total_steps} steps

Reward Breakdown:
   • Goal Reward:      +100
   • Step Cost:        {step_costs}
   • Hazard Penalty:   {hazard_penalties}
   • Total Reward:     {total_reward}

Mission Status:
   {mission_status}
"""
        
        ax3.text(0.1, 0.95, summary_text, transform=ax3.transAxes, 
                fontsize=11, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    if path is None:
        plt.tight_layout()
        plt.show()
        return None



    
    # 🎬 Animation with improved visuals
    if animate:
        xdata, ydata = [], []
        line, = ax.plot([], [], 'b-', linewidth=3, label='Path')
        agent, = ax.plot([], [], 'ro', markersize=10, label='Agent')

        def update(frame):
            x, y = path[frame]
            xdata.append(y)
            ydata.append(x)
            line.set_data(xdata, ydata)
            agent.set_data([y], [x])
            return line, agent

        ani = animation.FuncAnimation(
            fig,
            update,
            frames=len(path),
            interval=800,
            repeat=False
        )




        
        # 🔥 IMPORTANT (prevents garbage collection)
        plt.tight_layout()

    else:
        xs = [p[1] for p in path]
        ys = [p[0] for p in path]
        ax.plot(xs, ys, 'b-', linewidth=2, label='Path')
        ax.plot(xs[0], ys[0], 'go', markersize=12, label='Start')
        ax.plot(xs[-1], ys[-1], 'r*', markersize=20, label='End')
        ax.legend()
        plt.tight_layout()


    
    # Add restart buttons to all visualizations
    plt.subplots_adjust(bottom=0.15)
    
    restart_choice = {'value': None}
    
    def on_restart(event):
        restart_choice['value'] = 'yes'
        plt.close()
    
    def on_exit(event):
        restart_choice['value'] = 'no'
        plt.close()
    
    ax_restart = plt.axes([0.3, 0.05, 0.15, 0.05])
    ax_exit = plt.axes([0.55, 0.05, 0.15, 0.05])
    
    btn_restart = Button(ax_restart, '🔄 Restart', color='lightblue', hovercolor='skyblue')
    btn_exit = Button(ax_exit, '❌ Exit', color='lightcoral', hovercolor='salmon')
    
    btn_restart.on_clicked(on_restart)
    btn_exit.on_clicked(on_exit)
    
    plt.show()
    return restart_choice['value']
