import unittest
from prims import Prims
from objects import Room, Vertex, Edge, Triangle

rooms = []
rooms.append(Room(1,1))
rooms.append(Room(4,1))
rooms.append(Room(1,3))

triangles = [Triangle(Vertex(60, 60), Vertex(180, 60), Vertex(60, 140))]

class TestPrims(unittest.TestCase):
    def setUp(self):
        self.prims = Prims(rooms, triangles)

    def test_find_edges(self):
        edges = self.prims.find_edges()
        self.assertEqual(edges[(60, 60)], set([(180, 60), (60, 140)]))
        self.assertEqual(edges[(180, 60)], set([(60, 60), (60, 140)]))
        self.assertEqual(edges[(60, 140)], set([(60, 60), (180, 60)]))

    def test_add_edges_to_matrix(self):
        self.prims.add_edges_to_matrix()
        correct_matrix = [[0, 120.0, 80.0], [120.0, 0, 144.22205101855957], [80.0, 144.22205101855957, 0]]

        self.assertEqual(self.prims.adj_matrix, correct_matrix)

    def test_mst(self):
        edges = self.prims.mst()
        correct_edges = [((180, 60), (60, 60)), ((60, 140), (60, 60))]

        self.assertEqual(edges, correct_edges)