import pygame
pygame.init() 
scr = pygame.display.set_mode()
x, y = scr.get_size() 
pygame.display.quit() 
print(x, y)