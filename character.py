import pygame
import constants
import os

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.size = 20
        self.inventory = {"wood": 0}
        image_path = os.path.join("assets", 'images','character', "character.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.player, constants.player))
        self.size = self.image.get_width()
    
    def draw(self, screen):
        # Draw the character as a rectangle
        screen.blit(self.image, (self.x, self.y))

    def move(self, dx, dy):
        # Move the character by dx and dy
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, constants.width - self.size))
        self.y = max(0, min(self.y, constants.height - self.size))

        