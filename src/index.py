import pygame
from bowyer_watson import BowyerWatson
from objects import Room

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

    bowyer_watson = BowyerWatson(rooms)

    triangles = bowyer_watson.triangulate()

    for room in rooms:
        pygame.draw.rect(display, green, room.get_rect())
        pygame.draw.circle(display, red, room.find_center().to_tuple(), 2)

    for triangle in triangles:
        pygame.draw.line(display, red, triangle.v1.to_tuple(), triangle.v2.to_tuple())
        pygame.draw.line(display, red, triangle.v2.to_tuple(), triangle.v3.to_tuple())
        pygame.draw.line(display, red, triangle.v3.to_tuple(), triangle.v1.to_tuple())

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
