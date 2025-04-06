import pygame
import constants
from elements import Tree
import random
import os

# Representa el mundo del juego
class World:
    # Se ejecuta cuando se crea un nuevo mundo, se le pasa el tamaño de la pantalla
    def __init__(self, width, height):
        # Guarda el tamaño de la pantalla
        self.width = width
        self.height = height
        # Crea una lista de 10 árboles en posiciones aleatorias.
        # Se usa width - 40 y height - 40 para evitar que los árboles se dibujen fuera de la pantalla.
        # Crea 10 instancias de Tree
        self.trees = [Tree(random.randint(0, width-40), 
                      random.randint(0, height-40)) for _ in range(10)]
        # Ruta al archivo de imagen del pasto
        grass_path = os.path.join("assets", 'images','objects', "grass.png")
        # Carga la imagen del pasto (sin canal alfa ya que no necesita transparencia)
        self.grass_image = pygame.image.load(grass_path).convert()
        # Escala la imagen de pasto al tamaño definido en constants.grass, para que se repita de forma uniforme
        self.grass_image = pygame.transform.scale(self.grass_image, (constants.grass, constants.grass))

    # Dibuja el mundo en la pantalla
    def draw(self, screen):
        # Pinta el fondo del mundo con bloques de pasto.
        # Recorre todo el width y height en pasos del tamaño del pasto (constants.grass).
        # Coloca la imagen de pasto en cada posición como si fuera una "alfombra de tiles".
        for y in range(0, self.height, constants.grass):
            for x in range(0, self.width, constants.grass):
                screen.blit(self.grass_image, (x, y))


        # Dibuja todos los árboles en la pantalla, llamando al método draw de cada objeto Tree.
        for tree in self.trees:
            tree.draw(screen)

