import unittest
from math import sqrt
from objects import Vertex, Edge

v1 = Vertex(0,0)
v2 = Vertex(4,4)

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.edge = Edge(v1, v2)
        
    def test_get_length(self):
        length = self.edge.length()
        self.assertEqual(length, sqrt(32))
