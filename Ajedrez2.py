import pygame,sys
from pygame.locals import *

pygame.init()

Ventana = pygame.display.set_mode((560,560))
pygame.display.set_caption("Ajedrez")

Negro = (0,0,0)
Blanco = (255,255,255)


class Pieza():

	def __init__(self,nombre,color):
		self.Nombre = nombre
		self.Color = color

	def move(self):
		pass


class Peon(Pieza):

	def __init__(self,nombre,color):
		Parent.__init__(self,nombre,color)
		if self.Color == "Blanco":
			pass 

	def move(self):
		pass


class Caballo(Pieza):

	def __init__(self,nombre,color):
		Parent.__init__(self,nombre,color)

	def move(self):
		pass


class Reina(Pieza):

	def __init__(self,nombre,color):
		Parent.__init__(self,nombre,color)

	def move(self):
		pass


class Chess_Board():

	def __init__(self):
		Tablero = []
		Columnas = []
		Filas = []

	def draw_chess_board(self,Ventana,Dimension):
		Color = 0
		for Fila in range(8):
			for Columna in range(8):
				X,Y = Fila * Dimension, Columna * Dimension
				Columnas = [X,Y]
				Filas.append(Columnas)
				Columnas = []
				if Color % 2 == 0:
					pygame.draw.rect(Ventana,Negro,(X,Y,Dimension,Dimension))
				else:
					pygame.draw.rect(Ventana,Blanco,(X,Y,Dimension,Dimension))
				Color += 1
			Color += 1
			Tablero.append(Filas)
			Filas = []

#peon = pygame.image.load("Imagenes/Peon_Blanco.png")

chess = Chess_Board()

while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	chess.draw_chess_board(Ventana,70)
	#Ventana.blit(peon,(0,0))

	pygame.display.update()

