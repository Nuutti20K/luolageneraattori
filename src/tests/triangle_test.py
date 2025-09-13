import unittest
from objects import Vertex, Triangle

v1 = Vertex(0,0)
v2 = Vertex(0,4)
v3 = Vertex(4,4)

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(v1, v2, v3)
        
    def test_find_circumcenter(self):
        center_vertex = self.triangle.find_circumcenter()
        coordinates = (center_vertex.x, center_vertex.y)
        self.assertEqual(coordinates, (2,2))
