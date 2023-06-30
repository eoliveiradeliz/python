import pygame 
pygame.init() 
scr = pygame.display.set_mode((500,500))
pi = 3.14 
white = (255, 255, 255) 
pygame.draw.arc(scr, white, [210, 100, 250, 200], 0, pi / 2, 2)  
pygame.display.flip() 
while True:
  pass