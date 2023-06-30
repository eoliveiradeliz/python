import pygame, sys
pygame.init()
screen = pygame.display.set_mode((500, 400))
font = pygame.font.SysFont('arial', 18)
new_font = pygame.font.SysFont('Timesnewroman', 25)
new_font2 = pygame.font.SysFont('impact', 70)
text = font.render("Bem vindo ao Pygame ",True, (0,255,0))
fun = new_font.render("Enjoy with games", True, (0,255,255))
game_end = new_font2.render("Game Enéias", True, (255,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    screen.fill((255, 255, 255)) 
    screen.blit(text, (40,60))
    screen.blit(fun, (40,90))
    screen.blit(game_end, (40,140))
    pygame.display.flip()