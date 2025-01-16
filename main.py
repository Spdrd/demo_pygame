import pygame
import ctypes
import sys
import win32gui
import win32con

# Inicializar pygame
pygame.init()

# Obtener las dimensiones de la pantalla
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

print(f"{WIDTH}, {HEIGHT}")

# Configuración de la ventana (maximizada)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Ventana Transparente con Bola Azul Visible")

# Colores
TRANSPARENT_COLOR = (0,0,0)  # Negro será el color clave (transparente)
BLUE = (0, 0, 255)  # Color de la bola azul

# Configuración para maximizar la ventana y hacerla transparente en Windows
if sys.platform == "win32":
    hwnd = pygame.display.get_wm_info()["window"]

    # Llevar ventana al frente
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, WIDTH, HEIGHT, 0)

    # Estilo de ventana extendido
    WS_EX_LAYERED = 0x00080000
    GWL_EXSTYLE = -20
    ctypes.windll.user32.SetWindowLongW(
        hwnd, GWL_EXSTYLE, ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED
    )

    # Definir constantes de Windows
    HWND_TOPMOST = -10  # Constante para mantener la ventana al frente
    SWP_NOSIZE = 0x0001  # No cambiar el tamaño de la ventana
    SWP_NOMOVE = 0x0002  # No mover la ventana

    # Configurar la ventana como siempre al frente
    ctypes.windll.user32.SetWindowPos(
        hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE
    )

    # Configurar el color clave para la transparencia
    def RGB(r, g, b):
        return (r & 0xFF) | ((g & 0xFF) << 8) | ((b & 0xFF) << 16)

    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, RGB(*TRANSPARENT_COLOR), 0, 1)  # 1: Transparencia por color clave

# Posición inicial del círculo
circle_x, circle_y = 400, 300
circle_radius = 30
circle_speed_x, circle_speed_y = 5, 5

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el círculo
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # Rebotar en los bordes
    width, height = screen.get_size()
    if circle_x - circle_radius < 0 or circle_x + circle_radius > width:
        circle_speed_x = -circle_speed_x
    if circle_y - circle_radius < 0 or circle_y + circle_radius > height:
        circle_speed_y = -circle_speed_y

    # Dibujar en la pantalla
    screen.fill(TRANSPARENT_COLOR)  # Fondo transparente (color clave)
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)  # Bola azul visible


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle (FPS)
    clock.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()
