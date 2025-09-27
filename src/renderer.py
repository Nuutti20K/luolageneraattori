import pygame
from bowyer_watson import BowyerWatson
from prims import Prims
from randomize import generate_rooms


class Renderer:
    def __init__(self, display):
        self.display = display
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

    def render_rooms(self, amount):
        # Mielivaltainen lista neliskulmaisia huoneita
        # Toistaiseksi huoneet sijoittuvat 20x20 ruudukkoon

        rooms = generate_rooms(amount, 20)
        bowyer_watson = BowyerWatson(rooms)

        triangles = bowyer_watson.triangulate()

        prims = Prims(rooms, triangles)
        edges = prims.mst()

        self.display.fill((0,0,0))

        for room in rooms:
            pygame.draw.rect(self.display, self.green, room.get_rect())
            pygame.draw.circle(self.display, self.red, room.find_center().to_tuple(), 2)

        for triangle in triangles:
            pygame.draw.line(self.display, self.red, triangle.v1.to_tuple(), triangle.v2.to_tuple())
            pygame.draw.line(self.display, self.red, triangle.v2.to_tuple(), triangle.v3.to_tuple())
            pygame.draw.line(self.display, self.red, triangle.v3.to_tuple(), triangle.v1.to_tuple())

        for edge in edges:
            pygame.draw.line(self.display, self.blue, edge[0], edge[1], 3)

        pygame.display.update()

    def render_text(self, amount):
        font = pygame.font.SysFont("Arial", 48)

        text = font.render(amount, True, (255, 0, 0))
        pygame.draw.rect(self.display, (20, 20, 20), (800, 0, 200, 800))
        self.display.blit(text, (820, 351))
        pygame.display.update()
