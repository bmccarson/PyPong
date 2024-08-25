from settings import *
from support import import_image

class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
        self.direction = 0
        self.old_rect = self.rect.copy()

    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.get_direction()
        self.move(dt)
class Player(Paddle):
    def __init__(self, pos, groups, image):
        super().__init__(pos, groups, image)
        self.speed = SPEED['player']
         
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

class Opponent(Paddle):
    def __init__(self, pos, groups, image, ball):
        super().__init__(pos, groups, image)
        self.speed = SPEED['opponent']
        self.ball = ball
    
    def get_direction(self):
        self.direction = 1 if self.ball.rect.centery > self.rect.centery else -1
