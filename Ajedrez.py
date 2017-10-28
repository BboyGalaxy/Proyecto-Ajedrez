import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((560,560))
pygame.display.set_caption("Ajedrez")

blanco = (255,255,255)

coordenada_x = 0
coordenada_y = 0
for fila in range(0,8):
	if fila % 2 != 0:
		coordenada_x = coordenada_x = 70
	else:
		coordenada_x = 0
	for columna in range(0,8):
		pygame.draw.rect(ventana,blanco,(coordenada_x,coordenada_y,70,70))
		coordenada_x = coordenada_x + 140
	coordenada_y = coordenada_y + 70
	
	


while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()