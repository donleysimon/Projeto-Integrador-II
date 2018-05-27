import pygame
import color
import characters
import objects
import random

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
totalArvores = 5

fonte = pygame.font.SysFont("arial black", 34)
perdeu = pygame.font.SysFont("arial black", 52)

listaArvores = pygame.sprite.Group()
listaTotal = pygame.sprite.Group()

contar, texto = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 42)

class HitBox(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        skier = characters.Skier()
        self.image.set_colorkey((1,1,1))
        characters.Skier.down(skier, self.image, 0, 0)
        self.rect = self.image.get_rect()


    def update(self,x, y):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.x = x
        self.rect.y = y

hitBox_list = pygame.sprite.Group()
hitBox_Player = HitBox((1,1,1),34,62)
hitBox_list.add(hitBox_Player)

class HitBoxInimigo(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        yeti = characters.Monster()
        self.image.set_colorkey((1,1,1))
        characters.Monster.run(yeti, self.image, 0, 0)
        self.rect = self.image.get_rect()


    def update(self,x, y):
        """ Called each frame. """
        # Move block down one pixel
        self.rect.x = x
        self.rect.y = y

hitBoxInimigo_list = pygame.sprite.Group()
hitBoxInimigo_Player = HitBoxInimigo((1,1,1),34,62)
hitBoxInimigo_list.add(hitBoxInimigo_Player)

for i in range(totalArvores):
    tree = objects.Tree(color.colorKey, 44,22, velocidade, larguraTela)

    tree.rect.x = random.randrange(larguraTela)
    tree.rect.y = random.randrange(alturaTela)

    pedra = objects.Rock()

    objects.Rock.rock1(pedra, tree.image, 0, 0)
    screen.blit(tree.image, (tree.rect.x, tree.rect.y))

    listaArvores.add(tree)
    listaTotal.add(tree)

while jogoAtivo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False

        if evento.type == pygame.USEREVENT:
            contar -= 1
            texto = str(contar).rjust(3)

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

    hitBox_list.draw(screen)
    #Criacao de Personagem (fundo e personagem)
    player = pygame.Surface((34, 62))
    #player2 = pygame.Surface((42, 60))

    #Criacao das cores no Personagem
    #player.fill(color.colorKey)
    player.set_colorkey(color.colorKey)
    #player2.fill(color.colorKey)
    #player2.set_colorkey(color.colorKey)

    hitBox_list.update(posX - 17, posY - 31)
    #skier = characters.Skier()
    #characters.Skier.down(skier, player, 0, 0)
    #characters.Skier.playerDown(skier, player, 0, 0)
    #pygame.transform.scale(player, (42, 60), player2)
    #screen.blit(player, (posX - 17, posY - 31))

    blocks_hit_list = pygame.sprite.spritecollide(hitBox_Player, listaTotal, False)
    for block in blocks_hit_list:
        velocidade = 0

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

    # desenha tempo
    screen.blit(font.render(texto, True, (0, 0, 0)), (32, 48))
    # desenha inimigo
    if contar < 30:

        #pygame.draw.rect(screen, (100, 200, 200), [posXMonster, posYmonster, 40, 20])
        hitBoxInimigo_list.draw(screen)
        hitBoxInimigo_list.update(posXMonster, posYmonster)

        if velocidade < 10:
            if posXMonster > posX:
                posXMonster -= 25
            else:
                posXMonster += 25

            if posYmonster > posY:
                posYmonster -= 25
            else:
                posYmonster += 25
        elif velocidade > 10 and velocidade < 20:
            if posXMonster > posX:
                posXMonster -= 10
            else:
                posXMonster += 10

            if posYmonster> posY:
                posYmonster -= 10
            else:
                posYmonster += 10
        elif velocidade > 24 and contar > 25:
            if posXMonster > posX:
                posXMonster -= 1
            else:
                posXMonster += 1

            if posYmonster > posY:
                posYmonster -= 1
            else:
                posYmonster += 1
        else:
            posYmonster -= 2
            posXMonster -= 2

        teste = pygame.sprite.spritecollide(hitBoxInimigo_Player, hitBox_list, False)
        for inimigo in teste:
            screen.blit(font.render("PERDEU", True, (0, 0, 0)), (640, 360))
            #Perdeu e temporario
            velocidade = -50

    pygame.display.flip()

    clock.tick(30)

    pygame.display.flip()


pygame.quit()
