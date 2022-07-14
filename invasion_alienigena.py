import pygame
from pygame.sprite import Group

from configuraciones import Configuraciones

from estadisticas import Estadisticas

from nave import Nave

import funciones_juegos as fj

def run_game():

	# Inicializar el juego, las configuraciones y crear un objeto pantalla
	pygame.init()
	ai_configuraciones = Configuraciones()
	pantalla = pygame.display.set_mode(
		(ai_configuraciones.screen_width, ai_configuraciones.screen_height))
	pygame.display.set_caption("Invasión Alien")

	# Crea una instancia para guardar estadísticas del juego
	estadisticas = Estadisticas(ai_configuraciones)

	# Crea una nave, un grupo de balas y un grupo de enemigos
	nave = Nave(ai_configuraciones, pantalla)
	balas = Group()
	aliens = Group()


	# Crea la flota de enemigos
	fj.crear_flota(ai_configuraciones, pantalla, nave, aliens)

	# Iniciar el bucle principal del juego
	while True:

		# Escuchar eventos de teclado o ratón
		fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
		
		if estadisticas.game_active:
			nave.update()
			fj.update_balas(ai_configuraciones, pantalla, nave, aliens, balas)
			fj.update_aliens(ai_configuraciones, estadisticas, pantalla, nave, aliens, balas)

		fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, aliens, balas)

run_game()
