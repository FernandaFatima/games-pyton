import pygame
from pygame.locals import *
from sys import exit
from random import randint # Import necessary libraries

# Initialize Pygame
pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0 # Initialize points
font = pygame.font.SysFont("arial", 35, True, True) # Set the font for text display
# Create the game window
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Gaming Tester")
clock = pygame.time.Clock()
while True:
    tela.fill((0, 0, 0)) # Fill the screen with black
    mensagem = f'Pontos: {pontos}' # Create a message to display points
    texto_formatado = font.render(mensagem, True, (255, 255, 255)) # Render the text
    for event in pygame.event.get(): 
        if pygame.key.get_pressed()[K_a]: # Check for key presses
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20  
        if pygame.key.get_pressed()[K_s]:
            y = y + 20

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) # Draw a blue square
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) # Draw a smaller red square inside the blue square

    if ret_vermelho.colliderect(ret_azul): # Check for collision
        x_azul = randint(40, 600)
        y_azul = randint(50, 430) # Move the blue square to a new random position
        pontos = pontos + 1 # Increment points on collision
    tela.blit(texto_formatado, (450, 40)) # Draw the points on the screen


    pygame.display.update() # Update the display
    clock.tick(120) # Limit the frame rate to 60 FPS
