import unittest
from objects import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1,2,1,1)
        
    def test_find_center(self):
        center = self.room.find_center()
        self.assertEqual(center.x, 80)
        self.assertEqual(center.y, 60)

    def test_get_rect(self):
        rectangle = self.room.get_rect()
        self.assertEqual(rectangle[0], 40)
        self.assertEqual(rectangle[1], 40)
        self.assertEqual(rectangle[2], 80)
        self.assertEqual(rectangle[3], 40)