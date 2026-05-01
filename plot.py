import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def plot(history):
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    plt.savefig('fitness_plot.png')