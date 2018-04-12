import pygame
import color
import characters
import objects
import random

larguraTela = 600
alturaTela = 800

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((alturaTela, larguraTela))
pygame.display.set_caption("PyGame")
Dia = True
pygame.mouse.set_visible(True)
fake_screen = screen.copy()
jogoAtivo = True

posX = 400
posY = 300

velocidade = 1

#CriacaoObjetos
totalArvores = 5

listaArvores = pygame.sprite.Group()
listaTotal = pygame.sprite.Group()

for i in range(totalArvores):
    tree = objects.Tree(color.brown, 20, 20, velocidade, larguraTela)

    tree.rect.x = random.randrange(larguraTela)
    tree.rect.y = random.randrange(alturaTela)

    listaArvores.add(tree)
    listaTotal.add(tree)

while jogoAtivo:

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
    screen.fill(color.snow)

    #Criacao de Personagem (fundo e personagem)
    player = pygame.Surface((15, 30))
    player2 = pygame.Surface((20, 40))

    #Criacao das cores no Personagem
    player.fill(color.colorKey)
    player.set_colorkey(color.colorKey)
    player2.fill(color.colorKey)
    player2.set_colorkey(color.colorKey)


    skier = characters.Skier()
    characters.Skier.down(skier, player, 0, 0)
    pygame.transform.scale(player, (20, 40), player2)
    screen.blit(player2, (posX - 15, posY - 30))


    # Declara e atualiza posicao do mouse
    posMouse = pygame.mouse.get_pos()
    xMouse = posMouse[0]
    yMouse = posMouse[1]

    if yMouse > 300 :

        if velocidade < 25:
            velocidade += 0.1
        else:
            velocidade = 25
    else:
        if velocidade > 0:
            velocidade -= 0.5


    if xMouse > (posX + 50) :
        posX += 5
    elif xMouse < (posX - 50):
        posX -= 5


    for obj in listaArvores:
        obj.velocidade = velocidade

    listaTotal.update()

    listaTotal.draw(screen)

    clock.tick(30)

    pygame.display.flip()


pygame.quit()
