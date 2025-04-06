import pygame
import constants
from elements import Tree
import random
import os

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.trees = [Tree(random.randint(0, width-40), 
                      random.randint(0, height-40)) for _ in range(10)]
        
        grass_path = os.path.join("assets", 'images','objects', "grass.png")
        self.grass_image = pygame.image.load(grass_path).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constants.grass, constants.grass))

    def draw(self, screen):
        for y in range(0, self.height, constants.grass):
            for x in range(0, self.width, constants.grass):
                screen.blit(self.grass_image, (x, y))


        # Draw the trees
        for tree in self.trees:
            tree.draw(screen)

