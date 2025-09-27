import random
from objects import Room

def generate_rooms(amount, size):
    max_value = size * size
    values = random.sample(range(max_value), amount)
    rooms = []
    for value in values:
        rooms.append(Room(value // size, value % size))
    return rooms
