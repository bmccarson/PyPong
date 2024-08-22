from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('assets', 'players', 'Player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = SPEED['player'] 
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt
    
    def update(self, dt):
        self.input()
        self.move(dt)