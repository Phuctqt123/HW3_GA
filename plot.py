import matplotlib.pyplot as plt

def plot(history):
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    plt.show()