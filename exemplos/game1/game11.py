import pygame 
pygame.init() 
scr = pygame.display.set_mode((500,500)) 
lightgreen = (0, 255, 0) 
pygame.draw.polygon(scr, lightgreen, ((100, 100), (0, 200),(200, 200)), 3) 
pygame.display.flip() 
while True:
  pass