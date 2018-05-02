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
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.draw_piece()
		self.finding_move = False

		chess.piezas = []
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def find_move(self):
		print "buscando movimiento"
		new_fila = self.fila 
		new_columna = self.columna
	

		if self.color == "Blanco":
			if self.fila > 0:
				new_fila = self.fila - 1

		else:
			if self.fila < 7:
				new_fila = self.fila + 1

		coordenadas = chess.tablero[new_fila][new_columna]
		#color_objetivo = (255, 255, 50)
		#piece_objetivos.objetivos.append([self,coordenadas]) ----- original
		piece_objetivos.objetivos.append([self,[new_fila,new_columna]])
		#return [self,coordenadas]

	
		

class Caballo(Pieza):

	def __init__(self, nombre, color):
		Pieza.__init__(self,nombre,color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Caballo_Blanco.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 7
			self.columna = 4

		else:
			self.image = pygame.image.load("Imagenes/Caballo_Negro.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 0
			self.columna = 4
		self.finding_move = False

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.draw_piece()
		self.finding_move = False

		chess.piezas = []
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def draw_piece(self):
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

		

	def find_move(self):
		print "buscando movimiento"
		if self.fila - 2 > -1:
			if self.columna - 1 > -1:
				piece_objetivos.objetivos.append([self,[self.fila - 2,self.columna - 1]])
			if self.columna + 1 < 8:
				piece_objetivos.objetivos.append([self,[self.fila - 2,self.columna + 1]])

		if self.fila + 2 < 8:
			if self.columna - 1 > -1:
				piece_objetivos.objetivos.append([self,[self.fila + 2,self.columna - 1]])
			if self.columna + 1 < 8:
				piece_objetivos.objetivos.append([self,[self.fila + 2,self.columna + 1]])

		if self.columna - 2 > -1:
			if self.fila - 1 > -1:
				piece_objetivos.objetivos.append([self,[self.fila - 1,self.columna - 2]])
			if self.fila + 1 < 8:
				piece_objetivos.objetivos.append([self,[self.fila + 1,self.columna - 2]])

		if self.columna + 2 < 8:
			if self.fila - 1 > -1:
				piece_objetivos.objetivos.append([self,[self.fila - 1,self.columna + 2]])
			if self.fila + 1 < 8:
				piece_objetivos.objetivos.append([self,[self.fila + 1,self.columna + 2]])


class Reina(Pieza):

	def __init__(self, nombre, color):
		Pieza.__init__(self, nombre, color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Reina_Blanca.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 7
			self.columna = 5

		else:
			self.image = pygame.image.load("Imagenes/Reina_Negra.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = 0
			self.columna = 5
		self.finding_move = False

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.draw_piece()
		self.finding_move = False

		chess.piezas = []
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def draw_piece(self):
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def find_move(self):
		print "buscando movimiento"
		for count in range(8):
			if count != self.columna:
				piece_objetivos.objetivos.append([self,[self.fila,count]])
			if count != self.fila:
				piece_objetivos.objetivos.append([self,[count,self.columna]])
		for counter in range(1,9):
			if self.columna + counter < 8:
				if self.fila - counter  > -1:
					piece_objetivos.objetivos.append([self,[self.fila - counter, self.columna + counter]])
				if self.fila + counter < 8:
					piece_objetivos.objetivos.append([self,[self.fila + counter, self.columna + counter]])
			if self.columna - counter > -1:
				if self.fila - counter  > -1:
					piece_objetivos.objetivos.append([self,[self.fila - counter, self.columna - counter]])
				if self.fila + counter < 8:
					piece_objetivos.objetivos.append([self,[self.fila + counter, self.columna - counter]])

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
						count[0].finding_move = False
						piece_objetivos.objetivos = []
						print count[0].finding_move
						break

	def find_objetivos(self, posX, posY):
		for count in piece_objetivos.objetivos:
			coordenadas = self.tablero[count[1][0]][count[1][1]]
			if posX >= coordenadas[0] and posX <= coordenadas[0] + 70:
				if posY >= coordenadas[1] and posY <= coordenadas[1] + 70:
					count[0].move(count[1])
					piece_objetivos.objetivos = []


class Objetivo():

	def __init__(self):
		self.objetivos = []
		self.image = pygame.image.load("Imagenes/Objetivo.png")


chess = ChessBoard()
peon1 = Peon("peon1","Blano")
caballo1 = Caballo("caballo1","Blanco")
reina1 = Reina("reina1","Blanco")
piece_objetivos = Objetivo()



while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			posX,posY = pygame.mouse.get_pos()
			chess.find_piece(posX, posY)
			chess.find_objetivos(posX, posY)
			

	chess.draw_chess_board(Ventana, 70)
	#peon1.draw_piece()
	#caballo1.draw_piece()
	reina1.draw_piece()

	if len(piece_objetivos.objetivos) > 0:
		for count in piece_objetivos.objetivos:
			coordenadas = chess.tablero[count[1][0]][count[1][1]]
			Ventana.blit(piece_objetivos.image, (coordenadas[0],coordenadas[1], 70, 70))

	
	pygame.display.update()

