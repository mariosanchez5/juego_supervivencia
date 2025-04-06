import pygame
import sys #Se usa para cerrar el programa
import constants
from character import Character
from world import World

#Inicializar pygame
pygame.init()

#Crear la ventana del juego usando el tamaño definido en constants.py
screen = pygame.display.set_mode((constants.width,constants.height))

#Establecer el título de la ventana
pygame.display.set_caption("Simulador de vida salvaje")

def main():
    # Crear el reloj para controlar la velocidad de fotogramas
    clock = pygame.time.Clock()
    # Crear el mundo y el personaje
    world = World(constants.width, constants.height)
    # Crear el personaje en el centro de la pantalla
    character = Character(constants.width // 2, constants.height // 2)

    # Bucle principal del juego
    # Este bucle se ejecuta hasta que el usuario cierra la ventana o presiona la tecla de salida
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Detecta las teclas presionadas continuamente
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-5, 0)
        if keys[pygame.K_RIGHT]:    
            character.move(5, 0)
        if keys[pygame.K_UP]:
            character.move(0, -5)
        if keys[pygame.K_DOWN]:
            character.move(0, 5)
        # Mueve el personaje con las teclas de flecha, se desplaza 5 píxeles por pulsación

        # Dibuja el mundo y el personaje
        world.draw(screen)
        character.draw(screen)
        # Actualiza la pantalla con todo lo que se ha dibujado
        pygame.display.flip()
        # Limita la velocidad de fotogramas a 60 FPS, manteniendo el juego fluido
        clock.tick(60)

# Ejecuta la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
