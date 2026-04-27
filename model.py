import random
from data import *

def random_gene():
    return {
        "course": random.choice(courses),
        "section": random.choice(sections),
        "prof": random.choice(professors),
        "day": random.choice(days),
        "slot": random.choice(slots),
        "room": random.choice(rooms)
    }

def create_chromosome():
    # mỗi course có 2 sessions
    return [random_gene() for _ in range(NUM_COURSES * 2)]