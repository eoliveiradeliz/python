import pygame 
scr = pygame.display.set_mode((500, 400),pygame.RESIZABLE) 
pygame.display.set_caption('Resizable Window') 
running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
pygame.quit()