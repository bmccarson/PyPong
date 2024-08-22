from settings import *
from player import Player
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()

        # sprites
        self.BG = pygame.image.load(join('assets','board','Board.png')).convert_alpha()
        self.BG = pygame.transform.scale(self.BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.player = Player((30, WINDOW_HEIGHT / 2), self.all_sprites)
        self.ball = Ball(self.all_sprites)
    
    def run(self):
        while self.running:
            # dt 
            dt = self.clock.tick(FPS) / 1000

            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.blit(self.BG, (0,0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()