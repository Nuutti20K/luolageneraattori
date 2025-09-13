import unittest
from objects import Vertex

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex(1,2)
        
    def test_to_tuple(self):
        self.assertEqual(self.vertex.to_tuple(), (1,2))