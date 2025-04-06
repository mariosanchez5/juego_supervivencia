import pygame
import constants
import os

# Representa un personaje en el mundo del juego
class Character:
    # Se ejecuta cuando se crea un nuevo personaje, se le pasa la posicion en pantalla
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Inicializa el inventario del personaje
        self.inventory = {"wood": 0}
        # Construye la ruta de la imagen del personaje assets/images/character/character.png
        image_path = os.path.join("assets", 'images','character', "character.png")
        # Carga la imagen del personaje con transparencia (con convert_alpha)
        self.image = pygame.image.load(image_path).convert_alpha()
        # Cambia el tamaño de la imagen a las dimensiones definidas en constants.py
        self.image = pygame.transform.scale(self.image, (constants.player, constants.player))
        # Guarda el tamaño de la imagen, esto sirve para saber cuanto espacio ocupa en pantalla
        self.size = self.image.get_width()
    
    # Dibuja el personaje en la pantalla
    def draw(self, screen):
        # Dibuja el personaje en la posición (x, y)
        screen.blit(self.image, (self.x, self.y))

    # Mueve el personaje en la pantalla
    def move(self, dx, dy):
        # Mueve al personaje sumando desplazamientos dx (horizontal) y dy (vertical)
        self.x += dx
        self.y += dy
        # Limita el movimiento del personaje a la pantalla
        # max(0, ...): evita que se mueva a posiciones negativas.
        # min(..., constants.width - self.size): evita que se salga por el borde derecho o inferior.
        self.x = max(0, min(self.x, constants.width - self.size))
        self.y = max(0, min(self.y, constants.height - self.size))

        