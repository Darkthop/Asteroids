from CircleShape import CircleShape
import pygame
from constants import LINE_WIDTH,SHOT_RADIUS,PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self,screen : pygame.Surface):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)