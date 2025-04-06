import pygame
import constants
import os # Para construir rutas de archivos

# Representa un árbol en el mundo del juego
# Tiene una posición (x, y), imagen y una cantidad de madera
class Tree:
    # Se ejecuta cuando se crea un nuevo árbol, se le pasa la posicion en pantalla
    def __init__(self, x,y):
        self.x = x
        self.y = y
        # Cantidad de madera que da el árbol
        self.wood = 5

        # Construye la ruta de la imagen del árbol assets/images/objects/tree.png
        tree_path = os.path.join("assets", 'images','objects', "tree.png")
        # Carga la imagen del árbol con transparencia (con convert_alpha)
        self.image = pygame.image.load(tree_path).convert_alpha()
        # Cambia el tamaño de la imagen a las dimensiones definidas en constants.py
        self.image = pygame.transform.scale(self.image, (constants.tree, constants.tree))
        # Guarda el tamaño de la imagen, esto sirve para saber cuanto espacio ocupa en pantalla
        self.size = self.image.get_width()

    # Dibuja el árbol en la pantalla
    def draw(self, screen):
        # Dibuja el árbol en la posición (x, y)
        screen.blit(self.image, (self.x, self.y))
