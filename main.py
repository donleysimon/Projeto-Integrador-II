import pygame
import color
import characters
import objects
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame")
Dia = True
pygame.mouse.set_visible(False)
fake_screen = screen.copy()
player = pygame.surface.Surface((15, 30))
jogoAtivo = True
while jogoAtivo:
    screen.fill(color.blueSkyLight)



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
    player.fill(color.colorKey)
    player.set_colorkey(color.colorKey)
    player2.fill(color.colorKey)
    player2.set_colorkey(color.colorKey)
    skier = characters.Skier()
    characters.Skier.down(skier, player, 0, 0)
    pygame.transform.scale(player, (45, 90), player2)
    screen.blit(player2, (xMouse, yMouse))
    pygame.display.flip()

pygame.quit()
