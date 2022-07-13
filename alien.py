import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring: Sirve para representar un enemigo de la flota"""
	def __init__(self, ai_configuraciones, pantalla):
		"""Inicializa el enemigo y establece su posición inicial"""
		super(Alien, self).__init__()
	
		self.pantalla = pantalla
		self.ai_configuraciones = ai_configuraciones

		# Carga la imagen del enemigo y establece su atributo rect
		self.image = pygame.image.load("imagenes/alien.bmp")
		self.rect = self.image.get_rect()
		# self.pantalla_rect = pantalla.get_rect()

		# Inicia cada nuevo alien cerca de la parte superior izquierda
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Almacena la posición exacta del enemigo
		self.x = float(self.rect.x)

	def blitme(self):
		"""Dibuja el enemigo en su ubicación actual"""
		self.pantalla.blit(self.imagen, self.rect)

	def check_edges(self):
		"""Devuelve verdadero si el enemigo está en el borde de la pantalla"""
		screen_rect = self.pantalla.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

			
	def update(self):
		"""Mueve el enemigo a la derecha"""
		self.x += (self.ai_configuraciones.alien_speed_factor * 
					self.ai_configuraciones.fleet_direction)
		self.rect.x = self.x

