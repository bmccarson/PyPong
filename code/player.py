from settings import *
from support import import_image

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = import_image('assets', 'players', 'Player')
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = SPEED['player']
        self.old_rect = self.rect.copy() 
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)