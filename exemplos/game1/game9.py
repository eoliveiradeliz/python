import pygame 
pygame.init() 
scr = pygame.display.set_mode((500,500)) 
white = (255,255,255) 
pygame.draw.ellipse(scr, white , (350, 250, 60, 90), 4)
pygame.display.flip() 
while True:
  pass