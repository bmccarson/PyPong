from settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self, display_surface):
        super().__init__()
        self.score = {'player': 0, 'opponent': 0}
        self.font = pygame.font.Font(None, 160)
        self.display_surface = display_surface
    
    def display_score(self):
        # player
        player_score_surf = self.font.render(str(self.score['player']), True, 'White')
        player_score_rect = player_score_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_score_surf, player_score_rect)

        # opponent
        opponent_score_surf = self.font.render(str(self.score['opponent']), True, 'White')
        opponent_score_rect = player_score_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_score_surf, opponent_score_rect)
    
    def update(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1