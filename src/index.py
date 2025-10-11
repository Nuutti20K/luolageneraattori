import pygame
from renderer import Renderer
from game_loop import GameLoop



def main():
    pygame.init()
    display = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    renderer = Renderer(display)
    game_loop = GameLoop(clock, renderer)
    game_loop.start_game()

if __name__ == "__main__":
    main()
