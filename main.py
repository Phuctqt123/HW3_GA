from ga import run_ga
from plot import plot

best, history = run_ga()

print("Best schedule:")
for g in best:
    print(g)

plot(history)