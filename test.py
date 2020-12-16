if __name__ == '__main__':
    import pygame
    import sys

    pygame.init()
    pygame.display.set_mode((1200, 800))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    print(event.key)
