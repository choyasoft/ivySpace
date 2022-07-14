class Configuraciones():
	"""Sirve para almacenar todas las configs de Invasión Alien"""

	def __init__(self):
		"""Inicializa las configuraciones del juego"""

		self.screen_width = 900
		self.screen_height = 750
		self.bg_color = (230, 230, 230)
		
		# Configuraciones de la nave
		self.cantidad_naves = 3

		# Configuraciones de balas
		self.bala_width = 3
		self.bala_height = 15
		self.bala_color = 60, 60, 60
		self.balas_allowed = 3

		# Configuraciones de enemigo
		self.fleet_drop_speed = 5
		
		# Aceleración del juego tras pasar de nivel
		self.escala_aceleracion = 1.3
		# Aceleracion de los valores de score por nivel
		self.escala_puntaje = 1.5

		self.inicializa_configuraciones_dinamicas()

	def inicializa_configuraciones_dinamicas(self):
		"""Inicializa la configuración que cambia a lo largo del juego"""
		self.factor_velocidad_nave = 0.5
		self.bala_factor_velocidad = 0.7
		self.alien_speed_factor = 0.1

		# fleet_direction, cuando es 1 representa a la derecha. Cuando es -1 rep a la izquierda.
		self.fleet_direction = 1
		# Puntuación
		self.puntos_alien = 50

	def aumentar_velocidad(self):
		"""Aumenta la configuración de velocidad y los valores de puntos por enemigos"""
		self.factor_velocidad_nave *= self.escala_aceleracion
		self.bala_factor_velocidad *= self.escala_aceleracion
		self.alien_speed_factor *= self.escala_aceleracion

		self.puntos_alien = int(self.puntos_alien * self.escala_puntaje)
		print(self.puntos_alien)
