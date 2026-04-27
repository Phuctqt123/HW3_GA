import random
from model import create_chromosome
from fitness import fitness

POP_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:10]

def crossover(p1, p2):
    point = random.randint(0, len(p1)-1)
    return p1[:point] + p2[point:]

def mutate(chromosome):
    import copy
    from model import random_gene

    new = copy.deepcopy(chromosome)

    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(new)-1)
        new[idx] = random_gene()

    return new

def run_ga():
    population = [create_chromosome() for _ in range(POP_SIZE)]
    history = []

    for gen in range(GENERATIONS):
        population = selection(population)

        best = fitness(population[0])
        history.append(best)

        new_pop = population[:]

        while len(new_pop) < POP_SIZE:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    return population[0], history