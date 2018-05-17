import pygame
import color
import random
import math

class Objects(pygame.sprite.Sprite):

#Objects file

#Tree

    def __init__(self, color, largura, altura, velocidade, larguraTela, listaTotal):

        super().__init__()

        self.image = pygame.Surface([largura, altura])
        self.image.set_colorkey((1, 1, 1))

        self.rect = self.image.get_rect()

        self.velocidade = velocidade
        self.larguraTela = larguraTela

        self.listaTotal = listaTotal


    def reset_pos(self):

        posIndisponivel = False

        posY = random.randrange(1000, 1200)
        posX = random.randrange(0, self.larguraTela)

        for item in self.listaTotal:
            distancia = math.sqrt(((posX - item.rect.x) * (posX - item.rect.x)) + ((posY - item.rect.y) * (posY - item.rect.y)))

            if distancia < 50:
                posIndisponivel = True


        if posIndisponivel == False:
            self.rect.y = posY
            self.rect.x = posX
        else:
            print("resetou")
            self.reset_pos()



    def update(self):
        self.rect.y -= self.velocidade

        if self.rect.y < 10:
            self.reset_pos()
#Dry Tree

#Rock
class Rock:
    def rock1(self, screen, x, y):
        size = 2
        width = 22
        height = 11
        tilemap = [[color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.black,color.black,color.black,color.black,color.black,color.black,color.black,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.black,color.black,color.black,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.black,color.black,color.black,color.black,color.black,color.black,color.colorKey,color.colorKey,color.colorKey,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.colorKey,color.black,color.black,color.grayDark,color.grayDark,color.grayDark,color.black,color.grayDark,color.grayLight,color.grayLight,color.black,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.black,color.black,color.colorKey,color.colorKey,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.colorKey,color.black,color.grayDark,color.grayLight,color.grayLight,color.grayLight,color.grayDark,color.black,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.black,color.grayDark,color.grayDark,color.black,color.black,color.colorKey,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.black,color.black,color.grayDark,color.grayDark,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.grayLight,color.grayLight,color.grayDark,color.black,color.black,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.black,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.grayDark,color.grayLight,color.grayDark,color.black,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.black,color.colorKey,color.colorKey],
                   [color.colorKey,color.colorKey,color.black,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.black,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.grayLight,color.black,color.grayDark,color.black,color.black,color.colorKey],
                   [color.colorKey,color.black,color.grayDark,color.black,color.grayDark,color.grayDark,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.black,color.colorKey],
                   [color.colorKey,color.black,color.grayDark,color.grayDark,color.grayLight,color.grayDark,color.black,color.grayDark,color.grayLight,color.grayLight,color.grayLight,color.black,color.black,color.grayLight,color.black,color.grayLight,color.grayLight,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.black,color.colorKey],
                   [color.black,color.black,color.grayLight,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayDark,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.black,color.grayDark,color.black,color.black],
                   [color.black,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.black,color.grayLight,color.grayLight,color.grayLight,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.black,color.grayDark,color.grayLight,color.grayLight,color.grayDark,color.grayDark,color.grayDark,color.black]
                   ]
        for row in range(height):
            for column in range (width):
                pygame.draw.rect(screen, tilemap[row][column], (column*size,row*size,size,size))



#Ramp

#Snowman

#Fake Yeti

#Soft Snow

