import sys

import pygame
from bala import Bala
from alien import Alien

def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
	"""Responde a las pulsaciones de teclas"""
	if event.key == pygame.K_RIGHT:
		nave.moving_right = True
	elif event.key == pygame.K_LEFT:
		nave.moving_left = True
	elif event.key == pygame.K_SPACE:
		fuego_bala(ai_configuraciones, pantalla, nave, balas)
		
def verificar_eventos_keyup(event, nave):
	"""Responde a las pulsaciones de teclas"""
	if event.key == pygame.K_RIGHT:
		nave.moving_right = False
	elif event.key == pygame.K_LEFT:
		nave.moving_left = False

def verificar_eventos(ai_configuraciones, pantalla, nave, balas):
	""" Responde a las pulsaciones de teclas y los eventos del ratón """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas)

		elif event.type == pygame.KEYUP:
			verificar_eventos_keyup(event, nave)


def actualizar_pantalla(ai_configuraciones, pantalla, nave, aliens, balas):
	"""Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""

	# Volver a dibujar la pantalla durante cada pasada de bucle
	pantalla.fill(ai_configuraciones.bg_color)
	# Vuelve a dibujar todas las balas detrás de la nave y de los extraterrestres
	for bala in balas.sprites():
		bala.draw_bala()
	nave.blitme()
	aliens.draw(pantalla)
	
	# Hacer visible la pantalla dibujada más reciente		
	pygame.display.flip()

def update_balas(ai_configuraciones, pantalla, nave, aliens, balas):
	"""Docstring Actualiza la posición de las balas y elimina las antiguas"""
	# Actualiza las posiciones de las balas
	balas.update()

	# Eliminar las balas que han desaparecido
	for bala in balas.copy():
		if bala.rect.bottom <= 0:
			balas.remove(bala)
	check_bala_alien_collisions(ai_configuraciones, pantalla, nave, aliens, balas)

def check_bala_alien_collisions(ai_configuraciones, pantalla, nave, aliens, balas):
	"""Responde a las colisiones entre balas y aliens"""
	# Elimina las balas y los enemigos que hayan colisionado
	# Comprueba si hay balas que hayan tocado enemigos
	# Si es asi, desaparece la bala y el enemigo
	collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
	if len(aliens) == 0:
		# Destruye las balas existentes y crea una nueva flota
		balas.empty()
		crear_flota(ai_configuraciones, pantalla, nave, aliens)


def fuego_bala(ai_configuraciones, pantalla, nave, balas):
	"""Dispara una bala si aún no ha alcanzado el límite"""
	# Crea una nueva bala y la agrega al grupo de balas
	if len(balas) < ai_configuraciones.balas_allowed:
		nueva_bala = Bala(ai_configuraciones, pantalla, nave)
		balas.add(nueva_bala)

def get_number_aliens_x(ai_configuraciones, alien_width):
	"""Determina el número de enemigos que caben en una fila"""
	available_space_x = ai_configuraciones.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_configuraciones, nave_height, alien_height):
		"""Determina el número de filas de enemigos"""
		available_space_y = (ai_configuraciones.screen_height - (3 * alien_height) - nave_height)
		number_rows = int(available_space_y / (2 * alien_height))
		return number_rows

def crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number):
	"""Crea un enemigo y lo coloca en la fila"""
	alien = Alien(ai_configuraciones, pantalla)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def crear_flota(ai_configuraciones, pantalla, nave, aliens):
	"""Crea una flota completa de enemigos"""
	# Crea un enemigo y encuentra el número de aliens seguidos
	# El espacio entre cada enemigo es igual a un ancho del enemigo
	alien = Alien(ai_configuraciones, pantalla)
	number_aliens_x = get_number_aliens_x(ai_configuraciones, alien.rect.width)
	number_rows = get_number_rows(ai_configuraciones, nave.rect.height, alien.rect.height)
	
	# Crea la flota de enemigos
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number)

def check_fleet_edges(ai_configuraciones, aliens):
	"""Responde de forma apropiada si algún enemigo ha llegado a un borde"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_configuraciones, aliens)
			break

def change_fleet_direction(ai_configuraciones, aliens):
	"""Desciende la flota de enemigos y cambia su dirección"""
	for alien in aliens.sprites():
		alien.rect.y += ai_configuraciones.fleet_drop_speed
		ai_configuraciones.fleet_direction *= -1

def update_aliens(ai_configuraciones, nave, aliens):
	"""Comprueba si la flota está al borde y actualiza las posiciones de todos los enemigos de la flota"""
	check_fleet_edges(ai_configuraciones, aliens)
	aliens.update()

	# Busca colisiones de enemigo-nave
	if pygame.sprite.spritecollideany(nave, aliens):
		print("¡La nave ha recibido daños!")