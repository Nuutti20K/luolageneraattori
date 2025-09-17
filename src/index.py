import pygame
import time
from bowyer_watson import super_triangle, bowyer_watson
from objects import Vertex, Edge, Triangle, Room

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

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 800))
    display.fill((0,0,0))

    green = (0, 255, 0)
    red = (255, 0, 0)

    for room in rooms:
        pygame.draw.rect(display, green, room.get_rect())
        pygame.draw.circle(display, red, room.find_center().to_tuple(), 2)

    triangle = super_triangle(rooms)
    triangle_points = [triangle.v1, triangle.v2, triangle.v3]
    for vertex in triangle_points:
        pygame.draw.circle(display, red, vertex.to_tuple(), 2)


    pygame.draw.circle(display, red, triangle.find_circumcenter().to_tuple(), 2)

    triangles = bowyer_watson(rooms)

    for triangle in triangles:
        pygame.draw.line(display, red, triangle.v1.to_tuple(), triangle.v2.to_tuple())
        pygame.draw.line(display, red, triangle.v2.to_tuple(), triangle.v3.to_tuple())
        pygame.draw.line(display, red, triangle.v3.to_tuple(), triangle.v1.to_tuple())

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()