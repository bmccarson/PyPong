from settings import *
from support import import_image

from groups import *

from players import Player, Opponent
from ball import Ball
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = AllSprites()
        self.player_sprites = PlayerSprites()

        # sprites
        BG = import_image('assets','board','Board')
        self.BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.player = Player((30, WINDOW_HEIGHT / 2), (self.all_sprites, self.player_sprites),
                             import_image('assets', 'players', 'Player'))
        self.ball = Ball(self.all_sprites, self.player_sprites)
        self.opponent = Opponent((WINDOW_WIDTH - 30, WINDOW_HEIGHT /2),
                                 (self.all_sprites, self.player_sprites),
                                 import_image('assets', 'players', 'Opponent'),
                                 self.ball)
        self.score = Score(self.display_surface)
    
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
            self.score.display_score()
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()