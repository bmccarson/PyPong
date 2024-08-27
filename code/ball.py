from settings import *
from support import import_image
from random import choice, uniform
from score import Score

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, player_sprites, score):
        super().__init__(groups)
        self.image = import_image('assets', 'ball', 'Ball')
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.player_sprites = player_sprites
        self.score = score

        # movement
        self.direction = pygame.Vector2(choice((1,-1)),uniform(0.7, 0.8) * choice((-1,1)))
        self.speed = SPEED['ball']
        self.old_rect = self.rect.copy()

    
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.player_collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.player_collision('vertical')

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
        
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
        
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
            self.score.update_score('player' if self.rect.centerx > WINDOW_WIDTH / 2 else 'opponent')
            self.reset()
    
    def player_collision(self, direction):
        for sprite in self.player_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                else:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y *= -1
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y *= -1

    def reset(self):
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            self.direction = pygame.Vector2(choice((1,-1)),uniform(0.7, 0.8) * choice((-1,1)))

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.wall_collision()
