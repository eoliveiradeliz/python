import pygame 
pygame.init() 
scr = pygame.display.set_mode((600,500)) 
purple = (102, 0, 102) 
pygame.draw.polygon(scr, purple, 
                    ((146, 0), (291, 106),(236, 277), (56, 277), (0, 106))) 
pygame.display.flip() 
while True:
  pass