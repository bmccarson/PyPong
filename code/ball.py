from settings import *
from random import choice, uniform

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('assets', 'ball', 'Ball.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # movement
        self.direction = pygame.Vector2(choice((1,-1)),uniform(0.7, 0.8) * choice((-1,1)))
        self.speed = SPEED['ball']
    
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt
    
    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
        
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
        
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

    def update(self, dt):
        self.move(dt)
        self.wall_collision()
