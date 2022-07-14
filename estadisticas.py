class Estadisticas():
	"""Seguimiento de las estadísticas del juego"""
	def __init__(self, ai_configuraciones):
		"""Docstring: Inicializa las estadisticas del juego"""
		self.ai_configuraciones = ai_configuraciones
		self.reset_stats()
		# Inicia el juego en un estado activo
		self.game_active = True
		

	def reset_stats(self):
		"""Inicializa estadísticas que pueden variar durante la partida"""
		self.naves_restantes = self.ai_configuraciones.cantidad_naves

