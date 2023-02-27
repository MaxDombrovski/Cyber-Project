import pygame
# from menu import menu


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Cap.png")
        self.center = [100, 200]

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y

    def draw(self, surf):
        surf.blit(self.image, self.center)


class Game(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.player = Player()

    def run(self):
        running = True
        while running:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            self.player.move(move_x * 2, move_y * 2)

            self.screen.fill([200, 200, 200])
            self.player.draw(self.screen)
            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
