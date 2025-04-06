import pygame
import constants
import os

class Tree:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        #self.size = 40
        self.wood = 5

        tree_path = os.path.join("assets", 'images','objects', "tree.png")
        self.image = pygame.image.load(tree_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.tree, constants.tree))
        self.size = self.image.get_width()

    def draw(self, screen):
        # Draw the tree
        #pygame.draw.rect(screen, constants.brown, (self.x, self.y, self.size, self.size))
        screen.blit(self.image, (self.x, self.y))
