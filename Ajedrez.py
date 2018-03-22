import pygame,sys
from pygame.locals import *

pygame.init()

Ventana = pygame.display.set_mode((560, 560))
pygame.display.set_caption("Ajedrez")

Negro = (0, 0, 0)
Blanco = (255, 255, 255)


class Pieza():

	def __init__(self, nombre, color):
		self.nombre = nombre
		self.color = color

	def move(self):
		pass


class Peon(Pieza):

	def __init__(self, nombre, color):
		Pieza.__init__(self, nombre, color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Peon_Blanco.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 7
			self.columna = 3

		else:
			self.image = pygame.image.load("Imagenes/Peon_Negro.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 0
			self.columna = 3
		self.finding_move = False

		#chess.piezas.append([self,chess.tablero[self.fila][self.columna]])
		
	def draw_piece(self):
		fila = chess.tablero[self.fila]
		coordenadas = fila[self.columna]
		Ventana.blit(self.image, coordenadas)
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def move(self):
		pass

	def find_move(self):
		print "buscando movimiento"
		if self.color == "Blanco":
			new_fila = self.fila - 1
			new_columna = self.columna
		else:
			new_fila = self.fila + 1
			new_columna = self.columna

		coordenadas = chess.tablero[new_fila]
		coordenadas = coordenadas[new_columna]
		color_objetivo = (255, 255, 50)
		pygame.draw.rect(Ventana, color_objetivo, (coordenadas[0], coordenadas[1], 70, 70))
		print coordenadas

	
		

class Caballo(Pieza):

	def __init__(self, nombre, color):
		Parent.__init__(self,nombre,color)

	def move(self):
		pass


class Reina(Pieza):

	def __init__(self, nombre, color):
		Parent.__init__(self, nombre, color)

	def move(self):
		pass


class ChessBoard():

	def __init__(self):
		self.tablero = []
		self.piezas = []

	def draw_chess_board(self, ventana, dimension):
		Color = 0
		filas = [] 
		for Fila in range(8):
			for Columna in range(8):
				X,Y = Columna * dimension, Fila * dimension
				filas.append([X, Y])
				if Color % 2 == 0:
					pygame.draw.rect(ventana, Blanco, (X, Y, dimension, dimension))
				else:
					pygame.draw.rect(ventana, Negro, (X, Y, dimension, dimension))
				Color += 1
			Color += 1
			self.tablero.append(filas)
			filas = []

	def find_piece(self, posX, posY):
		for count in self.piezas:
			coordenadas = count[1]
			if posX >= coordenadas[0] and posX <= coordenadas[0] + 70:
				if posY >= coordenadas[1] and posY <= coordenadas[1] + 70:
					if count[0].finding_move == False:
						count[0].finding_move = True
						count[0].find_move()
						print count[0].finding_move
						break
					else:
						self.finding_move = False
						print count[0].finding_move
						break


chess = ChessBoard()
peon1 = Peon("peon1","Blanco")



while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			posX,posY = pygame.mouse.get_pos()
			chess.find_piece(posX, posY)

	chess.draw_chess_board(Ventana, 70)
	peon1.draw_piece()
	
	pygame.display.update()

