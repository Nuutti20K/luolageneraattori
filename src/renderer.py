import pygame

class Renderer:
    def __init__(self, display):
        self.display = display
        self.dark_green = (0, 128, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

    def render_rooms(self, dungeon, bw_toggle, mst_toggle):

        self.display.fill((0,0,0))

        for path in dungeon.paths:
            rect = (path[0] - 20, path[1] - 20, 40, 40)
            pygame.draw.rect(self.display, self.dark_green, rect)

        for room in dungeon.rooms:
            pygame.draw.rect(self.display, self.green, room.get_rect())

        if bw_toggle:
            for triangle in dungeon.triangles:
                v1 = triangle.v1.to_tuple()
                v2 = triangle.v2.to_tuple()
                v3 = triangle.v3.to_tuple()
                pygame.draw.line(self.display, self.red, v1, v2, 3)
                pygame.draw.line(self.display, self.red, v2, v3, 3)
                pygame.draw.line(self.display, self.red, v3, v1, 3)

        if mst_toggle:
            for edge in dungeon.edges:
                pygame.draw.line(self.display, self.blue, edge[0], edge[1], 5)

        pygame.display.update()

    def render_text(self, amount):
        font = pygame.font.SysFont("Arial", 48)

        text = font.render(amount, True, (255, 0, 0))
        pygame.draw.rect(self.display, (20, 20, 20), (800, 0, 200, 800))
        self.display.blit(text, (820, 351))
        pygame.display.update()
