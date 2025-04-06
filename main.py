import pygame
import sys
import constants
from character import Character
from world import World

#Inicializar pygame
pygame.init()

#Crear la ventana
screen = pygame.display.set_mode((constants.width,constants.height))

#Establecer el título de la ventana
pygame.display.set_caption("Simulador de vida salvaje")

def main():
    clock = pygame.time.Clock()
    world = World(constants.width, constants.height)
    character = Character(constants.width // 2, constants.height // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-5, 0)
        if keys[pygame.K_RIGHT]:    
            character.move(5, 0)
        if keys[pygame.K_UP]:
            character.move(0, -5)
        if keys[pygame.K_DOWN]:
            character.move(0, 5)

        world.draw(screen)
        character.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
