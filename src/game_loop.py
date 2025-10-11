import pygame
from dungeon import Dungeon

class GameLoop:
    def __init__(self, clock, renderer):
        self.clock = clock
        self.renderer = renderer
        self.amount = "10"
        self.running = True
        self.toggle = True
        self.dungeon = Dungeon(10)

    def start_game(self):
        while self.running:
            self.handle_events()
            self.renderer.render_text(self.amount)
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.amount != "" and int(self.amount) >= 3:
                    self.dungeon = Dungeon(int(self.amount))
                    self.renderer.render_rooms(self.dungeon, self.toggle)
                elif event.key == pygame.K_BACKSPACE and len(self.amount) > 0:
                    self.amount = self.amount[:-1]
                elif event.key == pygame.K_SPACE:
                    self.toggle = not self.toggle
                    self.renderer.render_rooms(self.dungeon, self.toggle)
                elif (len(self.amount) <= 10 and event.key != pygame.K_BACKSPACE and
                     event.unicode in "0123456789" and int(self.amount + event.unicode) <= 400):
                    self.amount += event.unicode
            if event.type == pygame.QUIT:
                self.running = False
