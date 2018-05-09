import pygame
import color
import random

class Tree(pygame.sprite.Sprite):

#Objects file

#Tree

    def __init__(self, color, largura, altura, velocidade, larguraTela):

        super().__init__()

        self.image = pygame.Surface([largura, altura])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.velocidade = velocidade
        self.larguraTela = larguraTela

    def reset_pos(self):
        self.rect.y = random.randrange(1000, 1200)
        self.rect.x = random.randrange(0, self.larguraTela)


    def update(self):
        self.rect.y -= self.velocidade

        if self.rect.y < 10:
            self.reset_pos()


#Dry Tree

#Rock
class Rock:
    def rock1(self, screen, x, y):
        size = 1
        width = 21
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

