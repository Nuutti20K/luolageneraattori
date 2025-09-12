from room import Room
from objects import Vertex, Edge, Triangle

points = []

def super_triangle(rooms):
    for room in rooms:
        points.append(room.find_center().to_tuple())

    x_list = []
    y_list = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])

    x_max = max(x_list)
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)

    # Etsitään pienin neliö, jonka sisään kaikki pisteet mahtuvat
    # Tämän perusteella voidaan etsiä tasasivuisen kolmion pisteet, minkä kanta ja korkeus on kaksinkertainen neliöön verrattuna

    square_width = max([(x_max - x_min), (y_max - y_min)])
    point_a = Vertex(int(x_min - 0.5 * square_width), y_min)
    point_b = Vertex(int(x_min + 1.5 * square_width), y_min)
    point_c = Vertex(int(x_min + 0.5 * square_width), int(y_min + 2 * square_width))

    return Triangle(point_a, point_b, point_c)


def bowyer_watson():
    pass