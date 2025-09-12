import pygame
from room import Room

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
    display = pygame.display.set_mode((400, 400))
    display.fill((0,0,0))

    green = (0, 255, 0)
    red = (255, 0, 0)

    square_size = 20

    for room in rooms:
        pygame.draw.rect(display, green, room.get_rect(square_size))
        pygame.draw.circle(display, red, room.find_center(square_size), 2)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()