import pygame
import color
import characters
import objects

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("PyGame")
sky = color.blueSkyLight
R, G, B = 80, 120, 200
BLACK = 0, 0, 0
RED = 255, 0, 0
Dia = True
pygame.mouse.set_visible(False)

fake_screen = screen.copy()
player = pygame.surface.Surface((15, 30))


jogoAtivo = True
while jogoAtivo:
    screen.fill(sky)

    bloco = pygame.Rect(200, 200, 150, 150)
    porta = pygame.Rect(220,300,25,50)
    janela = pygame.Rect(270, 310, 25, 25)
    janela2 = pygame.Rect(310, 310, 25, 25)
    janela3 = pygame.Rect(310, 230, 25, 25)
    janela4 = pygame.Rect(270, 230, 25, 25)
    janela5 = pygame.Rect(220, 230, 25, 25)
    pygame.draw.rect(screen, (200, 200, 200), bloco)
    pygame.draw.rect(screen,(10,10,10),porta)
    pygame.draw.rect(screen,(255,255,255),janela)
    pygame.draw.rect(screen, (255, 255, 255), janela2)
    pygame.draw.rect(screen, (255, 255, 255), janela3)
    pygame.draw.rect(screen, (255, 255, 255), janela4)
    pygame.draw.rect(screen, (255, 255, 255), janela5)



    pygame.draw.polygon(screen,(150,150,150),[(200,200),(275,150),(350,200)],0)




    for evento in pygame.event.get():
        #print(evento)
        if evento.type == pygame.QUIT:
            jogoAtivo = False
        if evento.type == pygame.KEYDOWN:
            print("Uma tecla foi pressionada")
        if evento.type == pygame.KEYUP:
            print("Uma tecla foi liberada")
            if evento.key == pygame.K_ESCAPE:
                jogoAtivo = False
            if evento.key == pygame.K_SPACE:
                if Dia:
                    sky = color.black
                    Dia = False
                else:
                    sky = color.blueSkyLight
                    Dia = True
    posMouse = pygame.mouse.get_pos()
    xMouse = posMouse[0]
    yMouse = posMouse[1]
    player = pygame.Surface((15, 30))
    player2 = pygame.Surface((45, 90))
    player.fill(color.azure)
    player.set_colorkey(color.azure)
    player2.fill(color.azure)
    player2.set_colorkey(color.azure)
    characters.Skier.down(player, 0, 0, 1)
    pygame.transform.scale(player, (45, 90), player2)
    screen.blit(player2, (xMouse, yMouse))
    pygame.display.flip()

pygame.quit()
