import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)
	def update(self, dt):
		movement = self.velocity * dt
		self.position += movement
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20,50)
		new1 = self.velocity.rotate(random_angle)
		new2 = self.velocity.rotate(-random_angle)
		new_size = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid1 = Asteroid(self.position.x, self.position.y, new_size)
		new_asteroid2 = Asteroid(self.position.x, self.position.y, new_size)
		new_asteroid1.velocity = new1 * 1.2
		new_asteroid2.velocity = new2 * 1.2
		return new_asteroid1, new_asteroid2

