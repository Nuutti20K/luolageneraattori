square_size = 10

# Huoneella on vasemman ylänurkan koordinaatit sekä leveys ja korkeus

class Room:
    def __init__(self, x, width, y, height):
        self.x = x
        self.width = width
        self.y = y
        self.height = height

    def find_center(self, mult):
        center_x = self.width * mult // 2 + self.x * mult
        center_y = self.height * mult // 2 + self.y * mult
        return (center_x, center_y)

    def get_rect(self, mult):
        x1 = self.x * mult
        y1 = self.y * mult
        width = self.width * mult
        height = self.height * mult
        return (x1, y1, width, height)

# Mielivaltainen lista neliskulmaisia huoneita
# Toistaiseksi huoneet sijoittuvat 20x20 ruudukkoon

rooms = []
rooms.append(Room(1,2,1,2))
rooms.append(Room(2,1,5,2))
rooms.append(Room(1,3,10,3))
rooms.append(Room(5,2,15,1))
rooms.append(Room(7,1,3,2))
rooms.append(Room(15,1,9,2))
rooms.append(Room(7,1,18,1))
rooms.append(Room(10,4,10,2))
rooms.append(Room(17,2,18,1))
rooms.append(Room(15,3,2,5))