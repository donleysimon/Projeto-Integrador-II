import pygame
import color
import characters
import objects
import random

larguraTela = 800
alturaTela = 600

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

velocidade = 1

#CriacaoObjetos
totalArvores = 5

listaArvores = pygame.sprite.Group()
listaTotal = pygame.sprite.Group()

class HitBox(pygame.sprite.Sprite):
    '''This class represents the ball
    It derives from the "Sprite" class in Pygame
    '''


    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        #self.image.fill(color)
        skier = characters.Skier()
        self.image.set_colorkey((1,1,1))
        characters.Skier.playerDown(skier, self.image, 0, 0)


        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


    def update(self,x, y):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.x = x
        self.rect.y = y

hitBox_list = pygame.sprite.Group()
hitBox_Player = HitBox((1,1,1),34,62)
hitBox_list.add(hitBox_Player)

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
    skier = characters.Skier()
    #characters.Skier.down(skier, player, 0, 0)
    characters.Skier.playerDown(skier, player, 0, 0)
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

    clock.tick(30)

    pygame.display.flip()


pygame.quit()
