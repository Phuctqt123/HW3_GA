import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use('Agg')

def plot(history):
    # Tạo folder outputs nếu chưa tồn tại
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    plt.figure(figsize=(10, 6))
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    plt.grid(True)
    
    output_path = os.path.join('outputs', 'fitness_plot.png')
    plt.savefig(output_path)
    print(f"The plot has been saved to: {output_path}")