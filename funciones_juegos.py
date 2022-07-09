import sys

import pygame

def verificar_eventos(nave):
	""" Responde a las pulsaciones de teclas y los eventos del ratón """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				nave.moving_right = True
			elif event.type == pygame.K_LEFT:
				nave.moving_left = False

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				nave.moving_right = False
			elif event.key == pygame.K_LEFT:
				nave.moving_left = False

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
	"""Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""

	# Volver a dibujar la pantalla durante cada pasada de bucle
	pantalla.fill(ai_configuraciones.bg_color)
	nave.blitme()

	# Hacer visible la pantalla dibujada más reciente		
	pygame.display.flip()