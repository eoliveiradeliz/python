import pygame 
pygame.init() 
scr = pygame.display.set_mode((500,500)) 
color = (0,0,255) 
pygame.draw.rect(scr, color, pygame.Rect(60, 60, 100, 100)) 
pygame.display.flip() 
while True:
  pass