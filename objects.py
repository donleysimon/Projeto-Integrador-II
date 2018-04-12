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

#Ramp

#Snowman

#Fake Yeti

#Soft Snow

