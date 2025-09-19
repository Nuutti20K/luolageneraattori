import math

# Huoneella on vasemman ylänurkan koordinaatit sekä leveys ja korkeus
# Huoneen ulottuvuudet kerrotaan square_size muutujalla kun niitä käsitellään pelialueella

class Room:
    def __init__(self, x, width, y, height):
        self.x = x
        self.width = width
        self.y = y
        self.height = height
        self.square_size = 40

    def find_center(self):
        center_x = self.width * self.square_size // 2 + self.x * self.square_size
        center_y = self.height * self.square_size // 2 + self.y * self.square_size
        return Vertex(center_x, center_y)

    def get_rect(self):
        x = self.x * self.square_size
        y = self.y * self.square_size
        width = self.width * self.square_size
        height = self.height * self.square_size
        return (x, y, width, height)

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def length(self):
        length = math.sqrt(abs(self.v1.x - self.v2.x)**2 + abs(self.v1.y - self.v2.y)**2)
        return length
    
    def __eq__(self, other):
        return (self.v1 == other.v1 and self.v2 == other.v2) or (self.v2 == other.v1 and self.v1 == other.v2)

class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def find_circumcenter(self):
        ax = self.v1.x
        ay = self.v1.y
        bx = self.v2.x
        by = self.v2.y
        cx = self.v3.x
        cy = self.v3.y
        
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
        uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
        return Vertex(ux, uy)
    
    def inside_circumcircle(self, vertex):
        center = self.find_circumcenter()
        radius = Edge(self.v1, center).length()
        vertex_distance = Edge(vertex, center).length()
        return vertex_distance < radius