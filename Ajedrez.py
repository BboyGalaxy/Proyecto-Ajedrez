import pygame,sys
from pygame.locals import *

pygame.init()

Ventana = pygame.display.set_mode((560, 560))
pygame.display.set_caption("Ajedrez")

Negro = (0, 0, 0)
Blanco = (255, 255, 255)

fuente = pygame.font.Font(None, 50)
texto = fuente.render('Elija una pieza', 1, (255, 255, 255))

class Pieza():

	def __init__(self, color):

		self.color = color
		self.objetivos = []
		self.image_objetivos = pygame.image.load("Imagenes/Objetivo.png")

	def move(self):
		pass

	def change_position(self, posX, posY):
		for count in chess.piezas:
			if count[0] == self:
				count[1] = chess.tablero[posX][posY]

	def verify_colision(self, fila, columna):
		position_ocuped = False
		for count in chess.piezas:
			if count[1] == chess.tablero[fila][columna]:
				position_ocuped = True
		return position_ocuped

	def change_behavior(self):
		for count in chess.piezas:
			if count[0] != self:
				count[0].finding_move = False
				count[0].objetivos = []

class Peon(Pieza):

	def __init__(self, color, fila, columna):
		Pieza.__init__(self, color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Peon_Blanco.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = fila
			self.columna = columna

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

			if self.columna > 0:
				self.objetivos.append([self,[new_fila,new_columna - 1]])
			if self.columna < 7:
				self.objetivos.append([self,[new_fila,new_columna + 1]])


	
		

class Caballo(Pieza):

	def __init__(self, color, fila, columna):
		Pieza.__init__(self, color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Caballo_Blanco.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = fila
			self.columna = columna

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

	def __init__(self, color, fila, columna):
		Pieza.__init__(self, color)
		if self.color == "Blanco":
			self.image = pygame.image.load("Imagenes/Reina_Blanca.png")
			self.image = pygame.transform.scale(self.image, (70, 70))
			self.fila = fila
			self.columna = columna

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

		for count in range(self.fila + 1,8):
			if self.verify_colision(count,self.columna) == False:
				self.objetivos.append([self,[count, self.columna]])
			else:
				break

		count = self.fila - 1
		while(count > -1):
			if self.verify_colision(count,self.columna) == False:
				self.objetivos.append([self,[count, self.columna]])
			else:
				break
			count -= 1

		for count in range(self.columna + 1 , 8):
			if self.verify_colision(self.fila,count) == False:
				self.objetivos.append([self,[self.fila, count]])
			else:
				break

		count = self.columna - 1
		while(count > -1):
			if self.verify_colision(self.fila,count) == False:
				self.objetivos.append([self,[self.fila, count]])
			else:
				break
			count -= 1

		fila_objetivo = self.fila
		for count in range(self.columna + 1 , 8):
			fila_objetivo -= 1
			if fila_objetivo > -1:
				if self.verify_colision(fila_objetivo, count) == False:
					self.objetivos.append([self,[fila_objetivo, count]])
				else:
					break

		fila_objetivo = self.fila
		for count in range(self.columna + 1 , 8):
			fila_objetivo += 1
			if fila_objetivo < 8:
				if self.verify_colision(fila_objetivo, count) == False:
					self.objetivos.append([self,[fila_objetivo, count]])
				else:
					break

		fila_objetivo = self.fila
		count = self.columna - 1
		while(count > -1):
			fila_objetivo -= 1
			if fila_objetivo > -1:
				if self.verify_colision(fila_objetivo, count) == False:
					self.objetivos.append([self,[fila_objetivo, count]])
				else:
					break
			count -= 1

		fila_objetivo = self.fila
		count = self.columna - 1
		while(count > -1):
			fila_objetivo += 1
			if fila_objetivo < 8:
				if self.verify_colision(fila_objetivo, count) == False:
					self.objetivos.append([self,[fila_objetivo, count]])
				else:
					break
			count -= 1

class ChessBoard():

	def __init__(self):
		self.tablero = []
		self.piezas = []
		self.menu = True
		self.fila_piece = 4
		self.col_piece = 3
		

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

		for pieza in self.piezas:
			pieza[0].draw_piece()

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

	def draw_menu(self):
		Ventana.fill((0,0,0))
		Ventana.blit(texto,(140,50))
		peon = pygame.image.load("Imagenes/Peon_Blanco.png")
		peon = pygame.transform.scale(peon, (70, 70))
		caballo = pygame.image.load("Imagenes/Caballo_Blanco.png")
		caballo = pygame.transform.scale(caballo, (70, 70))
		reina = pygame.image.load("Imagenes/Reina_Blanca.png")
		reina = pygame.transform.scale(reina, (70, 70))
		Ventana.blit(peon, (50, 200))
		Ventana.blit(caballo, (220, 200))
		Ventana.blit(reina, (400,  200))


	def draw_piece(self, posX, posY):
		if len(chess.piezas) == 5:
			self.menu = False
			return

		if posX >= 50 and posX <= 120:
			if posY >= 200 and posY <= 270:
				piece = Peon("Blanco",self.fila_piece, self.col_piece)
		if posX >= 220 and posX <= 290:
			if posY >= 200 and posY <= 270:
				piece = Caballo("Blanco",self.fila_piece, self.col_piece)
		if posX >= 400 and posX <= 470:
			if posY >= 200 and posY <= 270:
				piece = Reina("Blanco",self.fila_piece, self.col_piece)

		self.menu = False

	def add_or_replace(self, posx, posy):
		posicion = 0
		delete = False

		for count in chess.piezas:
			coordenadas = count[1]
			if posx >= coordenadas[0] and posx <= coordenadas[0] + 70:
				if posy >= coordenadas[1] and posy <= coordenadas[1] + 70:
					delete = True
					break
			posicion += 1

		if delete:
			chess.piezas.pop(posicion)


	def get_filcol(self, posx, posy):
		set_fila = 0
		set_columna = 0
		for filas in chess.tablero:
			for columnas in filas:
				if posx >= columnas[0] and posx <= columnas[0] + 70:
					if posy >= columnas[1] and posy <= columnas[1] + 70:
						self.fila_piece = set_fila
						self.col_piece = set_columna
						print self.fila_piece, self.col_piece
						return
				set_columna += 1
			set_fila += 1
			set_columna = 0



chess = ChessBoard()
chess.draw_chess_board(Ventana, 70)



while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:

			posX,posY = pygame.mouse.get_pos()

			if evento.button == 1 and chess.menu == False:
				chess.find_piece(posX, posY)
				chess.find_objetivos(posX, posY)

			elif evento.button == 3:
				print "Elegir pieza"
				chess.add_or_replace(posX, posY)
				chess.get_filcol(posX, posY)
				
				if chess.menu:
					chess.menu = False
				else:
					chess.menu = True

			else:
				chess.draw_piece(posX, posY)

	if chess.menu:
		chess.draw_menu()
	else:
		chess.draw_chess_board(Ventana, 70)
		

	if len(chess.piezas) > 0:
		for count in chess.piezas:
			if len(count[0].objetivos) > 0:
				for objetives in count[0].objetivos:
					coordenadas = chess.tablero[objetives[1][0]][objetives[1][1]]
					Ventana.blit(count[0].image_objetivos, (coordenadas[0],coordenadas[1], 70, 70))

	print len(chess.piezas)
	#print chess.tablero
	pygame.display.update()

