import pygame

# Inicializar pygame
pygame.init()

# Configuración de la ventana sin bordes
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
pygame.display.set_caption("Ventana sin bordes")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar algo en la ventana
    screen.fill((0, 128, 255))  # Color de fondo
    pygame.display.flip()

pygame.quit()
