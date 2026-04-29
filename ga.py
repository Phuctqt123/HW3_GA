import random
from model import create_chromosome
from fitness import fitness
import copy
from data import *
POP_SIZE = 200
GENERATIONS = 50
MUTATION_RATE = 0.4

def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:50]
def tournament_selection(population, k=3):
    # Chọn ngẫu nhiên k cá thể, ai tốt nhất thì thắng
    selected = random.sample(population, k)
    selected.sort(key=fitness, reverse=True)
    return selected[0]

def crossover(p1, p2):
    size = len(p1)
    # Chọn 2 điểm ngẫu nhiên
    pt1 = random.randint(0, size - 2)
    pt2 = random.randint(pt1 + 1, size - 1)

    # Ghép: Đầu của p1 + Giữa của p2 + Cuối của p1
    return p1[:pt1] + p2[pt1:pt2] + p1[pt2:]

def mutate(chromosome):
    new = copy.deepcopy(chromosome)
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(new) - 1)
        choice = random.choice(["section", "prof", "day", "slot", "room"])
        if choice == "section":
            new[idx]["section"] = random.choice(sections)
        elif choice == "prof":
            new[idx]["prof"] = random.choice(professors)
        elif choice == "day":
            new[idx]["day"] = random.choice(days)
        elif choice == "slot":
            new[idx]["slot"] = random.choice(slots)
        elif choice == "room":
            new[idx]["room"] = random.choice(rooms)
    return new

def hill_climbing_refine(individual):
    """
    Thử thay đổi nhẹ cá thể tốt nhất để xem có cải thiện được không
    (Tư duy tìm kiếm lân cận)
    """
    best_temp = individual
    current_fit = fitness(individual)

    for _ in range(5):  # Thử 5 lần tinh chỉnh nhanh
        refined = mutate(best_temp)
        if fitness(refined) > current_fit:
            best_temp = refined
            current_fit = fitness(refined)
    return best_temp
def run_ga():
    population = [create_chromosome() for _ in range(POP_SIZE)]
    history = []
    best = -float('inf')
    while best < 0:
        population = selection(population)

        best = fitness(population[0])
        if best > -100:
            best_individual = hill_climbing_refine(population[0])
            best = fitness(best_individual)
        history.append(best)

        # Giữ nguyên 2 cá thể tốt nhất, không cho đột biến
        new_pop = [copy.deepcopy(population[0]), copy.deepcopy(population[1])]

        while len(new_pop) < POP_SIZE:
            p1 = tournament_selection(population)
            p2 = tournament_selection(population)
            child = crossover(p1, p2)
            child = mutate(child)  # Chỉ mutate con cái
            new_pop.append(child)

        population = new_pop

    return population[0], history