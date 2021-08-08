
import pygame,


class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 0.3

        size = self.game.screen.get_size()

        self.pos = pygame.math.Vector2(size[0]/2, size[1]/2)
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(pygame.math.Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(pygame.math.Vector2(0, self.speed))
        if pressed[pygame.K_d]:
            self.add_force(pygame.math.Vector2(self.speed, 0))
        if pressed[pygame.K_a]:
            self.add_force(pygame.math.Vector2(-self.speed, 0))
        # Physics
        self.vel *= 0.8
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        # Base triangle
        points = [pygame.math.Vector2(-7, -7), pygame.math.Vector2(-1.4, -7), pygame.math.Vector2(-1.4, -14), pygame.math.Vector2(1.4, -14), pygame.math.Vector2(1.4, -7),pygame.math.Vector2(7, -7), pygame.math.Vector2(7, 7), pygame.math.Vector2(-7, 7)]
        # Rotate points
        angle = self.vel.angle_to(pygame.math.Vector2(0, 1))
        points = [p.rotate(angle) for p in points]
        # Fix y axis
        points = [pygame.math.Vector2(p.x, p.y * -1) for p in points]
        # Add currant position
        points = [self.pos + p * 2 for p in points]
        # Draw triangle
        pygame.draw.polygon(self.game.screen, (0, 100, 255), points)
