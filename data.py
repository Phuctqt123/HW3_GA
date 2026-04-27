from data_loader import load_data

data = load_data()

rooms = data["rooms"]
courses = data["courses"]
professors = data["professors"]
days = data["days"]
slots = data["slots"]
sections = data["sections"]

NUM_COURSES = len(courses)
NUM_ROOMS = len(rooms)
NUM_PROFESSORS = len(professors)
NUM_DAYS = len(days)
NUM_SLOTS = len(slots)
NUM_SECTIONS = len(sections)