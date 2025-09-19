import unittest
from bowyer_watson import BowyerWatson
from objects import Room, Vertex, Edge, Triangle

rooms = []
rooms.append(Room(1,1,1,1))
rooms.append(Room(3,1,13,1))
rooms.append(Room(15,1,15,1))

class TestBowyerWatson(unittest.TestCase):
    def setUp(self):
        self.bowyer_watson = BowyerWatson(rooms)

    def test_super_triangle(self):
        st = self.bowyer_watson.super_triangle()
        self.assertTrue(st.v1 == Vertex(-2740, -2740))
        self.assertTrue(st.v2 == Vertex(5660, -2740))
        self.assertTrue(st.v3 == Vertex(-2740, 5660))

    def test_unique_edges(self):
        edges = []
        edges.append(Edge(1,5))
        edges.append(Edge(5,1))
        edges.append(Edge(3,1))
        edges.append(Edge(3,5))
        uniques = self.bowyer_watson.unique_edges(edges)
        self.assertEqual(len(uniques), 2)

    def test_add_vertex(self):
        triangles = [Triangle(Vertex(1,6), Vertex(6,6), Vertex(3,1))]
        vertex = Vertex(3,3)
        result = self.bowyer_watson.add_vertex(vertex, triangles)
        self.assertEqual(len(result), 3)

    def test_add_vertex_not_in_circumcircle(self):
        triangles = [Triangle(Vertex(1,6), Vertex(6,6), Vertex(3,1))]
        vertex = Vertex(7,7)
        result = self.bowyer_watson.add_vertex(vertex, triangles)
        self.assertEqual(len(result), 1)

    def test_triangulate(self):
        result = self.bowyer_watson.triangulate()
        print(result[0].v1, result[0].v2, result[0].v3)
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].v1 == Vertex(140,540))
        self.assertTrue(result[0].v2 == Vertex(60,60))
        self.assertTrue(result[0].v3 == Vertex(620,620))


        