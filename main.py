import pygame
import color
import characters
import objects
import random

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('nevada.mp3')

pygame.mixer.music.play(-1)


#pygame.mixer.music.play(1,0)

larguraTela = 1280
alturaTela = 720

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("PyGame")
Dia = True
pygame.mouse.set_visible(True)
fake_screen = screen.copy()
jogoAtivo = True

posX = 400
posY = 300

posXMonster = 1800
posYmonster = 1800
posicaoAlex = random.randrange(0, 2)
posicaoAleY = random.randrange(0, 2)

acabou = 50
acaba = 0

if(posicaoAlex < 1):
    posXmonster = 0
else:
    posXMonster = 1300

if(posicaoAleY < 1):
    posYmonster = 0
else:
    posYmonster = 800

velocidade = 1

#CriacaoObjetos
totalPedras = 4
totalArvoresG = 5
totalArvoresPequenas = 5
totalBuracoNeve = 5
totalRampas = 5
totalPlacas = 8
posicionaPlacas = 0

fonte = pygame.font.SysFont("arial black", 34)
perdeu = pygame.font.SysFont("arial black", 52)

listaArvores = pygame.sprite.Group()
listaPedras = pygame.sprite.Group()
listaObjetosAleatorios = pygame.sprite.Group()
listaBuracos = pygame.sprite.Group()
listaTotal = pygame.sprite.Group()

contar, texto = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 42)

pulei = False
puloBloqueado = False
tempoPulo = 1
bloqueiaPulo = 2
tempoColisao = 2
colidi = False
tempoComeu = 10
comeu = False



class HitBox(pygame.sprite.Sprite):
    def __init__(self, color):

        super().__init__()

        self.image = pygame.Surface([34, 62])
        self.image.set_colorkey((1, 1, 1))
        self.rect = self.image.get_rect()


    def update(self,x, y):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.x = x
        self.rect.y = y


    def animacoes(self, animacao):
        skier = characters.Skier()

        if animacao == 0:
            self.image = pygame.Surface([32, 62])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.down(skier, self.image, 0, 0)


        if animacao == 1:
            self.image = pygame.Surface([48, 55])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.right2(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)


        if animacao == 2:
            self.image = pygame.Surface([48, 55])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.right2(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, True, False)

        if animacao == 3:
            self.image = pygame.Surface([48, 55])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.right3(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)

        if animacao == 4:
            self.image = pygame.Surface([48, 55])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.right3(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, True, False)

        if animacao == 5:
            self.image = pygame.Surface([64, 64])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.jump(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)

        if animacao == 6:
            self.image = pygame.Surface([60, 60])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.hitting(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)

        if animacao == 7:
            self.image = pygame.Surface([60, 60])
            self.image.set_colorkey((1, 1, 1))
            characters.Skier.onFloor(skier, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)


hitBox_list = pygame.sprite.Group()
hitBox_Player = HitBox((1,1,1))
hitBox_list.add(hitBox_Player)
animacaoPlayer = 0

class HitBoxInimigo(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        yeti = characters.Monster
        self.image.set_colorkey((1,1,1))
        characters.Monster.yetiCelebrate(yeti, self.image, 0, 0)
        self.rect = self.image.get_rect()


    def update(self,x, y):
        """ Called each frame. """
        # Move block down one pixel
        self.rect.x = x
        self.rect.y = y

    def animacoes(self, animacao):
        moster = characters.Monster()

        if animacao == 0:
            self.image = pygame.Surface([50, 86])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiRun(moster, self.image, 0, 0)

        if animacao == 1:
            self.image = pygame.Surface([58, 75])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiEating1(moster, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)

        if animacao == 2:
            self.image = pygame.Surface([40, 80])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiEating2(moster, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, True, False)

        if animacao == 3:
            self.image = pygame.Surface([40, 73])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiEating3(moster, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, False, False)

        if animacao == 4:
            self.image = pygame.Surface([64, 80])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiCelebrate(moster, self.image, 0, 0)

        if animacao == 5:
            self.image = pygame.Surface([50, 86])
            self.image.set_colorkey((1, 1, 1))
            characters.Monster.yetiRun(moster, self.image, 0, 0)
            self.image = pygame.transform.flip(self.image, True, False)

hitBoxInimigo_list = pygame.sprite.Group()
hitBoxInimigo_Player = HitBoxInimigo((1,1,1),34,64)
hitBoxInimigo_list.add(hitBoxInimigo_Player)
animacaoInimigo = 0

for i in range(totalPedras):
    pedras = objects.Tree(color.colorKey, 44,22, velocidade, larguraTela)

    pedras.reset_pos()

    pedra = objects.Rock()

    objects.Rock.rock1(pedra, pedras.image, 0, 0)
    screen.blit(pedras.image, (pedras.rect.x, pedras.rect.y))

    listaPedras.add(pedras)
    listaTotal.add(pedras)

for i in range(totalArvoresG):
    arvoreGigante = objects.Tree(color.colorKey, 30,63, velocidade, larguraTela)

    arvoreGigante.reset_pos()

    arvoreS = objects.Rock()

    objects.Rock.treeGiant(arvoreGigante, arvoreGigante.image, 0, 0)
    screen.blit(arvoreGigante.image, (arvoreGigante.rect.x, arvoreGigante.rect.y))

    listaArvores.add(arvoreGigante)
    listaTotal.add(arvoreGigante)



for i in range(totalPedras):
    pedras2 = objects.Tree(color.colorKey, 32,24, velocidade, larguraTela)

    pedras2.reset_pos()

    pedraTwo = objects.Rock()

    objects.Rock.rock2(pedras2, pedras2.image, 0, 0)
    screen.blit(pedras2.image, (pedras2.rect.x, pedras2.rect.y))

    listaPedras.add(pedras2)
    listaTotal.add(pedras2)

for i in range(totalBuracoNeve):
    buraco = objects.Tree(color.colorKey, 50,24, velocidade, larguraTela)

    buraco.reset_pos()

    buracoNeve = objects.Rock()

    objects.Rock.snowSoft2(buraco, buraco.image, 0, 0)
    screen.blit(buraco.image, (buraco.rect.x, buraco.rect.y))

    listaBuracos.add(buraco)
    listaTotal.add(buraco)

for i in range(totalRampas):
    rampas = objects.Tree(color.colorKey, 60,14, velocidade, larguraTela)

    rampas.reset_pos()

    rampasGrandes = objects.Rock()

    objects.Rock.ramp(rampas, rampas.image, 0, 0)
    screen.blit(rampas.image, (rampas.rect.x, rampas.rect.y))

    listaObjetosAleatorios.add(rampas)

for i in range(totalPlacas):
    placas = objects.Tree(color.colorKey, 42,27, velocidade, larguraTela)

    placas.rect.y = 400
    placas.rect.x = posicionaPlacas

    placasGrandes = objects.Rock()

    objects.Rock.startSign(placas, placas.image, 0, 0)
    screen.blit(placas.image, (placas.rect.x, placas.rect.y))

    listaTotal.add(placas)
    posicionaPlacas += 200

'''for i in range(totalBuracoNeve):
    buraco = objects.Tree(color.colorKey, 50,24, velocidade, larguraTela)

    buraco.reset_pos()

    buracoNeve = objects.Rock()

    objects.Rock.snowSoft1(buraco, buraco.image, 0, 0)
    screen.blit(buraco.image, (buraco.rect.x, buraco.rect.y))

    listaBuracos.add(buraco)
    listaTotal.add(buraco)

for i in range(totalArvoresG):
    arvoreGigante = objects.Tree(color.colorKey, 30,63, velocidade, larguraTela)

    arvoreGigante.reset_pos()

    arvoreS = objects.Rock()

    objects.Rock.treeFire1(arvoreGigante, arvoreGigante.image, 0, 0)
    screen.blit(arvoreGigante.image, (arvoreGigante.rect.x, arvoreGigante.rect.y))

    listaArvores.add(arvoreGigante)
    listaTotal.add(arvoreGigante)'''



while jogoAtivo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False

        if evento.type == pygame.USEREVENT:
            contar -= 1
            texto = str(contar).rjust(3)

            if pulei == True:

                tempoPulo -= 1
                if tempoPulo <= 0:
                    tempoPulo = 1
                    pulei = False

            if puloBloqueado == True:

                bloqueiaPulo -= 1
                if bloqueiaPulo <= 0:
                    bloqueiaPulo = 2
                    puloBloqueado = False

            if colidi == True:

                tempoColisao -= 1
                if tempoColisao <= 0:
                    tempoColisao = 2
                    colidi = False


        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pulei == False and puloBloqueado == False:
                pulei = True
                puloBloqueado = True
                print("Pimba com segurança")


        #print(evento)

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
    player = pygame.Surface((34, 62))

    player.set_colorkey(color.colorKey)


    hitBox_list.update(posX - 17, posY - 31)

    hitBox_Player.animacoes(animacaoPlayer)
    hitBoxInimigo_Player.animacoes(animacaoInimigo)
    if comeu == False:
        hitBox_list.draw(screen)

    blocks_hit_list = pygame.sprite.spritecollide(hitBox_Player, listaTotal, False)
    for block in blocks_hit_list:
        if pulei == False and colidi == False:
            velocidade = 0
            colidi = True

    blockRampas = pygame.sprite.spritecollide(hitBox_Player, listaObjetosAleatorios, False)
    for block in blockRampas:
        if pulei == False and colidi == False:
            pulei = True

    # Declara e atualiza posicao do mouse
    posMouse = pygame.mouse.get_pos()
    xMouse = posMouse[0]
    yMouse = posMouse[1]

    if yMouse > 300 and comeu == False:

        if velocidade < 25:
            velocidade += 0.1
        else:
            velocidade = 25
    else:
        if velocidade > 0:
            velocidade -= 0.5

    if colidi == False and comeu == False:

        if pulei == False:

            if xMouse > (posX + 50):
                posX += 5
                if velocidade > 0:
                    animacaoPlayer = 1
                else:
                    animacaoPlayer = 3

            elif xMouse < (posX - 50):
                posX -= 5
                if velocidade > 0:
                    animacaoPlayer = 2
                else:
                    animacaoPlayer = 4
            else:
                animacaoPlayer = 0
        else:
            animacaoPlayer = 5
    else:
        animacaoPlayer = 6

    for obj in listaTotal:
        obj.velocidade = velocidade

    for obj in listaObjetosAleatorios:
        obj.velocidade = velocidade

    listaTotal.update()
    listaObjetosAleatorios.update()

    listaTotal.draw(screen)
    listaObjetosAleatorios.draw(screen)

    # desenha tempo
    screen.blit(font.render(texto, True, (0, 0, 0)), (32, 48))
    # desenha inimigo

    if contar < 55 and contar > 50:
        #pygame.draw.rect(screen, (100, 200, 200), [posXMonster, posYmonster, 40, 20])
        hitBoxInimigo_list.draw(screen)
        hitBoxInimigo_list.update(posXMonster, posYmonster)

        if velocidade < 10 and comeu == False:
            if posXMonster > posX:
                posXMonster -= 25
                animacaoInimigo = 5
            else:
                posXMonster += 25
                animacaoInimigo = 0
            if posYmonster > posY:
                posYmonster -= 25
            else:
                posYmonster += 25
        elif velocidade > 10 and velocidade < 20 and comeu == False:
            if posXMonster > posX:
                posXMonster -= 10
                animacaoInimigo = 5
            else:
                posXMonster += 10
                animacaoInimigo = 0
            if posYmonster> posY:
                posYmonster -= 10
            else:
                posYmonster += 10
        elif velocidade > 24 and contar > 25 and comeu == False:
            if posXMonster > posX:
                posXMonster -= 1
                animacaoInimigo = 5
            else:
                posXMonster += 1
                animacaoInimigo = 0
            if posYmonster > posY:
                posYmonster -= 1
            else:
                posYmonster += 1
        else:
            posYmonster -= 2
            posXMonster -= 2

        teste = pygame.sprite.spritecollide(hitBoxInimigo_Player, hitBox_list, False)
        for inimigo in teste:
            #screen.blit(font.render("PERDEU", True, (0, 0, 0)), (640, 360))
            #Perdeu e temporario
            tempoComeu -= 1
            comeu = True
            if tempoComeu < 10 and tempoComeu > 8:
                animacaoInimigo = 1
                pygame.mixer.music.load('gobble.wav')
                pygame.mixer.music.play(0)
            elif tempoComeu < 8 and tempoComeu > 6:
                animacaoInimigo = 2
            elif tempoComeu < 4 and tempoComeu > 2:
                animacaoInimigo = 3
            elif tempoComeu < 2 and tempoComeu > 0:
                animacaoInimigo = 4
                pygame.mixer.music.load('argh.wav')
                pygame.mixer.music.play(0)

            if acaba < acabou:
                acaba += 1

            if acaba == 50:
                jogoAtivo = False

    if contar <= 50:
        screen.blit(font.render("GANHOU", True, (0, 0, 0)), (640, 360))

        if acaba < acabou:
            acaba += 1

        if acaba == 50:
            jogoAtivo = False

    pygame.display.flip()

    clock.tick(30)

    pygame.display.flip()


pygame.quit()
