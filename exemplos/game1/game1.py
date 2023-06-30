# vamos importar as bibliotecas necessárias
import pygame, sys
from pygame.locals import *
 
# inicializa a biblioteca
pygame.init()
# obtém a superfície do jogo e define o tamanho da tela
DISPLAYSURF = pygame.display.set_mode((600, 600))
# vamos definir o título da janela do jogo
pygame.display.set_caption('Jogo de Cartas do Enéias')
 
# e aqui nós entramos no loop do game
while True:
  # monitoramos os eventos
  for evento in pygame.event.get():
   # se o evento foi um pedido para sair
   if evento.type == QUIT:
    # fechamos a tela do jogo 
    pygame.quit()
    # e saimos do programa
    sys.exit()
 
   # redesenha a tela continuamente 
   pygame.display.update()