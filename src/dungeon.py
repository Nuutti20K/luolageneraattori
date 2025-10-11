from bowyer_watson import BowyerWatson
from prims import Prims
from path_creator import PathCreator
from randomize import generate_rooms

class Dungeon:
    def __init__(self, amount):
        self.rooms = generate_rooms(amount, 20)
        bowyer_watson = BowyerWatson(self.rooms)

        self.triangles = bowyer_watson.triangulate()

        prims = Prims(self.rooms, self.triangles)
        self.edges = prims.mst()

        path_creator = PathCreator(self.edges)
        self.paths = path_creator.create_paths()
    