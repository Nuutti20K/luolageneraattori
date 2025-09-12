# Huoneella on vasemman ylänurkan koordinaatit sekä leveys ja korkeus
# Huoneen ulottuvuudet kerrotaan square_size parametrilla kun niitä käsitellään pelialueella

class Room:
    def __init__(self, x, width, y, height):
        self.x = x
        self.width = width
        self.y = y
        self.height = height

    def find_center(self, square_size):
        center_x = self.width * square_size // 2 + self.x * square_size
        center_y = self.height * square_size // 2 + self.y * square_size
        return (center_x, center_y)

    def get_rect(self, square_size):
        x = self.x * square_size
        y = self.y * square_size
        width = self.width * square_size
        height = self.height * square_size
        return (x, y, width, height)