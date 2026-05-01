import random
from data import *

def create_chromosome():
    chromosome = []
    # Lặp qua danh sách 15 môn học, mỗi môn tạo 2 gene
    for course in courses:
        for _ in range(2):
            gene = {
                "course": course, # Cố định môn học
                "section": random.choice(sections),
                "prof": random.choice(professors),
                "day": random.choice(days),
                "slot": random.choice(slots),
                "room": random.choice(rooms)
            }
            chromosome.append(gene)
    return chromosome