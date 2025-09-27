import pygame
from renderer import Renderer



def main():
    pygame.init()
    display = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    renderer = Renderer(display)

    running = True
    amount = "10"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and amount != "":
                    if int(amount) >= 3:
                        renderer.render_rooms(int(amount))
                elif event.key == pygame.K_BACKSPACE and len(amount) > 0:
                    amount = amount[:-1]
                elif len(amount) <= 10 and event.key != pygame.K_BACKSPACE:
                    # Kovakoodattu 400 pitää poistaa
                    if event.unicode in "0123456789" and int(amount + event.unicode) <= 400:
                        amount += event.unicode
            if event.type == pygame.QUIT:
                running = False
        renderer.render_text(amount)
        clock.tick(60)

if __name__ == "__main__":
    main()
