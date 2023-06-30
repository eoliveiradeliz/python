import pygame 
pygame.init() 
scr = pygame.display.set_mode((500,500)) 
color = (0,255,0) 
pygame.draw.line(scr, color, (40, 300), (140, 300), 6)
pygame.display.flip()
color = (0,254,0) 
pygame.draw.line(scr, color, (40, 400), (150, 400), 8)
pygame.display.flip() 
while True:
  pass