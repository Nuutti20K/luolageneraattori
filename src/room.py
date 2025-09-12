from objects import Vertex

# Huoneella on vasemman ylänurkan koordinaatit sekä leveys ja korkeus
# Huoneen ulottuvuudet kerrotaan square_size parametrilla kun niitä käsitellään pelialueella

class Room:
    def __init__(self, x, width, y, height):
        self.x = x
        self.width = width
        self.y = y
        self.height = height
        self.square_size = 20
        self.x_margin = 200

    def find_center(self):
        center_x = self.width * self.square_size // 2 + self.x * self.square_size + self.x_margin
        center_y = self.height * self.square_size // 2 + self.y * self.square_size
        return Vertex(center_x, center_y)

    def get_rect(self):
        x = self.x * self.square_size + self.x_margin
        y = self.y * self.square_size
        width = self.width * self.square_size
        height = self.height * self.square_size
        return (x, y, width, height)