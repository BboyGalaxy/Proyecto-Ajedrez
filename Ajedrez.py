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
		self.objetivos = []
		self.image_objetivos = pygame.image.load("Imagenes/Objetivo.png")

	def move(self):
		pass

	def change_position(self, posX, posY):
		for count in chess.piezas:
			if count[0].nombre == self.nombre:
				count[1] = chess.tablero[posX][posY]

	def verify_colision(self, fila, columna):
		position_ocuped = False
		for count in chess.piezas:
			if count[1] == chess.tablero[fila][columna]:
				position_ocuped = True
		return position_ocuped

	def change_behavior(self):
		for count in chess.piezas:
			if count[0].nombre != self.nombre:
				count[0].finding_move = False
				count[0].objetivos = []

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
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])
		
	def draw_piece(self):
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.finding_move = False

		self.change_position(self.fila,self.columna)

	def find_move(self):
		self.change_behavior()
		print "buscando movimiento"
		new_fila = self.fila 
		new_columna = self.columna
	

		if self.color == "Blanco":
			if self.fila > 0:
				new_fila = self.fila - 1

		else:
			if self.fila < 7:
				new_fila = self.fila + 1

		if self.verify_colision(new_fila, new_columna) == False:
			coordenadas = chess.tablero[new_fila][new_columna]
			
			self.objetivos.append([self,[new_fila,new_columna]])


	
		

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
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.finding_move = False

		self.change_position(self.fila, self.columna)

	def draw_piece(self):
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		

		

	def find_move(self):
		self.change_behavior()
		print "buscando movimiento"
		if self.fila - 2 > -1:
			if self.columna - 1 > -1:
				if self.verify_colision(self.fila - 2, self.columna - 1) == False:
					self.objetivos.append([self,[self.fila - 2,self.columna - 1]])
			if self.columna + 1 < 8:
				if self.verify_colision(self.fila - 2, self.columna + 1) == False:
					self.objetivos.append([self,[self.fila - 2,self.columna + 1]])

		if self.fila + 2 < 8:
			if self.columna - 1 > -1:
				if self.verify_colision(self.fila + 2 , self.columna - 1) == False:
					self.objetivos.append([self,[self.fila + 2,self.columna - 1]])
			if self.columna + 1 < 8:
				if self.verify_colision(self.fila + 2, self.columna + 1) == False:
					self.objetivos.append([self,[self.fila + 2,self.columna + 1]])

		if self.columna - 2 > -1:
			if self.fila - 1 > -1:
				if self.verify_colision(self.fila - 1, self.columna - 2) == False:
					self.objetivos.append([self,[self.fila - 1,self.columna - 2]])
			if self.fila + 1 < 8:
				if self.verify_colision(self.fila + 1, self.columna - 2) == False:
					self.objetivos.append([self,[self.fila + 1,self.columna - 2]])

		if self.columna + 2 < 8:
			if self.fila - 1 > -1:
				if self.verify_colision(self.fila - 1, self.columna + 2) == False:
					self.objetivos.append([self,[self.fila - 1,self.columna + 2]])
			if self.fila + 1 < 8:
				if self.verify_colision(self.fila + 1, self.columna + 2) == False:
					self.objetivos.append([self,[self.fila + 1,self.columna + 2]])


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
		chess.piezas.append([self,chess.tablero[self.fila][self.columna]])

	def move(self,coordenadas):
		print "se movio"
		self.fila = coordenadas[0]
		self.columna = coordenadas[1]
		self.finding_move = False

		self.change_position(self.fila, self.columna)

	def draw_piece(self):
		coordenadas = chess.tablero[self.fila][self.columna]
		Ventana.blit(self.image, coordenadas)
		

	def find_move(self):
		self.change_behavior()
		print "buscando movimiento"

		### hacer recorrido por cada posible ruta de movimiento para parar los objetivos en cuanto encuentre una colision (8 en total)

		for count in range(8):
			if count != self.columna:
				self.objetivos.append([self,[self.fila,count]])
			if count != self.fila:
				self.objetivos.append([self,[count,self.columna]])
		for counter in range(1,9):
			if self.columna + counter < 8:
				if self.fila - counter  > -1:
					self.objetivos.append([self,[self.fila - counter, self.columna + counter]])
				if self.fila + counter < 8:
					self.objetivos.append([self,[self.fila + counter, self.columna + counter]])
			if self.columna - counter > -1:
				if self.fila - counter  > -1:
					self.objetivos.append([self,[self.fila - counter, self.columna - counter]])
				if self.fila + counter < 8:
					self.objetivos.append([self,[self.fila + counter, self.columna - counter]])

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
						count[0].objetivos = []
						print count[0].finding_move
						break

	def find_objetivos(self, posX, posY):
		for pieza in self.piezas:
			if len(pieza[0].objetivos) > 0 :
				for count in pieza[0].objetivos:
					coordenadas = self.tablero[count[1][0]][count[1][1]]
					if posX >= coordenadas[0] and posX <= coordenadas[0] + 70:
						if posY >= coordenadas[1] and posY <= coordenadas[1] + 70:
							count[0].move(count[1])
							count[0].objetivos = []




chess = ChessBoard()
chess.draw_chess_board(Ventana, 70)
#peon1 = Peon("peon1","Blanco")
#peon2 = Peon("peon2","s")
#caballo1 = Caballo("caballo1","Blanco")
reina1 = Reina("reina1","Blanco")




while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			if evento.button == 1:
				posX,posY = pygame.mouse.get_pos()
				chess.find_piece(posX, posY)
				chess.find_objetivos(posX, posY)
			elif evento.button == 3:
				print "Elegir pieza"


	chess.draw_chess_board(Ventana, 70)
	#peon1.draw_piece()
	#peon2.draw_piece()
	#caballo1.draw_piece()
	reina1.draw_piece()

	if len(chess.piezas) > 0:
		for count in chess.piezas:
			if len(count[0].objetivos) > 0:
				for objetives in count[0].objetivos:
					coordenadas = chess.tablero[objetives[1][0]][objetives[1][1]]
					Ventana.blit(count[0].image_objetivos, (coordenadas[0],coordenadas[1], 70, 70))

	print len(chess.piezas)
	pygame.display.update()

