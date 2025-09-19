import unittest
from math import sqrt
from objects import Vertex, Edge

v1 = Vertex(0,0)
v2 = Vertex(4,4)
v3 = Vertex(2,2)

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.edge = Edge(v1, v2)
        self.reverse = Edge(v2, v1)
        self.different = Edge(v1, v3)
        
    def test_get_length(self):
        length = self.edge.length()
        self.assertEqual(length, sqrt(32))

    def test_is_equal(self):
        self.assertEqual(self.edge == self.edge, True)

    def test_reverse_is_equal(self):
        self.assertEqual(self.edge == self.reverse, True)

    def test_not_equal(self):
        self.assertEqual(self.edge == self.different, False)