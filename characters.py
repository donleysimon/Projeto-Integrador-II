#Characters file
import pygame
import color

#Skier
class Skier:

    def down(screen, x, y, size):
        #body principal
        corpo = pygame.Rect(3+x, 11+y, 9*size, 9*size)
        pygame.draw.rect(screen, color.blue, corpo)

        #head
        pompom = pygame.Rect(8+x, y*size, 2*size, 2*size)
        pygame.draw.rect(screen, color.blue, pompom)
        
        gorro = pygame.Rect(7+x, 2+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.red, gorro)
        gorro2 = pygame.Rect(6+x, 4+y, 3*size, 3*size)
        pygame.draw.rect(screen, color.red, gorro2)
        gorro3 = pygame.Rect(5+x, 7+y, 5*size, 1*size)
        pygame.draw.rect(screen, color.rose , gorro3)
        gorro4 = pygame.Rect(5+x, 8+y, 5*size, 1*size)
        pygame.draw.rect(screen, color.red, gorro4)
        gorro5 = pygame.Rect(4+x, 9+y, 7*size, 1*size)
        pygame.draw.rect(screen, color.red, gorro5)
        
        cabeca = pygame.Rect(5+x, 10+y, 5*size, 1*size)
        pygame.draw.rect(screen, color.beige, cabeca)
        cabeca1 = pygame.Rect(5+x, 13+y, 2*size, 2*size)
        pygame.draw.rect(screen, color.beige, cabeca1)
        cabeca2 = pygame.Rect(8+x, 13+y, 2*size, 2*size)
        pygame.draw.rect(screen, color.beige, cabeca2)
        cabeca3 = pygame.Rect(7+x, 12+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.beige, cabeca3)
        cabeca4 = pygame.Rect(6+x, 15+y, 3*size, 1*size)
        pygame.draw.rect(screen, color.beige, cabeca4)
        
        boca = pygame.Rect(7+x, 14+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.brown, boca)
        
        oculos = pygame.Rect(5+x, 11+y, 5*size, 1*size)
        pygame.draw.rect(screen, color.navy, oculos)
        oculos2 = pygame.Rect(5+x, 12+y, 2*size, 1*size)
        pygame.draw.rect(screen, color.navy, oculos2)
        oculos3 = pygame.Rect(8+x, 12+y, 2*size, 1*size)
        pygame.draw.rect(screen, color.navy, oculos3)

        #body
        braco = pygame.Rect(12+x, 12+y, 3*size, 3*size)
        pygame.draw.rect(screen, color.rose, braco)
        braco1 = pygame.Rect(1+x, 11+y, 2*size, 1*size)
        pygame.draw.rect(screen, color.rose, braco1)
        braco2 = pygame.Rect(1+x, 15+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.rose, braco2)
        
        bracoR = pygame.Rect(x, 12+y, 3*size, 3*size)
        pygame.draw.rect(screen, color.rose, bracoR)
        bracoR1 = pygame.Rect(12+x, 11+y, 2*size, 1*size)
        pygame.draw.rect(screen, color.rose, bracoR1)
        bracoR2 = pygame.Rect(13+x, 15+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.rose, bracoR2)
        
        luva = pygame.Rect(2+x, 15+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.red, luva)
        luva1 = pygame.Rect(2+x, 16+y, 2*size, 2*size)
        pygame.draw.rect(screen, color.red, luva1)
        
        luvaR = pygame.Rect(12+x, 15+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.red, luvaR)
        luvaR1 = pygame.Rect(11+x, 16+y, 2*size, 2*size)
        pygame.draw.rect(screen, color.red, luvaR1)
        
        corpo1 = pygame.Rect(2+x, 12+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.blue, corpo1)
        corpo2 = pygame.Rect(12+x, 12+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.blue, corpo2)
        
        #ski
        ski = pygame.Rect(2+x, 5+y, 3*size, 1*size)
        pygame.draw.rect(screen, color.black, ski)
        ski1 = pygame.Rect(3+x, 4+y, 1*size, 7*size)
        pygame.draw.rect(screen, color.black, ski1)
        ski2 = pygame.Rect(3+x, 14+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.black, ski2)
        ski3 = pygame.Rect(2+x, 18+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.black, ski3)
        
        skiR = pygame.Rect(10+x, 5+y, 3*size, 1*size)
        pygame.draw.rect(screen, color.black, skiR)
        skiR1 = pygame.Rect(11+x, 4+y, 1*size, 7*size)
        pygame.draw.rect(screen, color.black, skiR1)
        skiR2 = pygame.Rect(11+x, 14+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.black, skiR2)
        skiR3 = pygame.Rect(12+x, 18+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.black, skiR3)
        
        #legs Left
        leg = pygame.Rect(2+x, 20+y, 3*size, 4*size)
        pygame.draw.rect(screen, color.blue, leg)
        leg1 = pygame.Rect(5+x, 20+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.blue, leg1)
        

        #skis Left
        ski4 = pygame.Rect(2+x, 25+y, 3*size, 4*size)
        pygame.draw.rect(screen, color.black, ski4)
        ski5 = pygame.Rect(2+x, 29+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.black, ski5)
        ski6 = pygame.Rect(4+x, 29+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.black, ski6)
        ski7 = pygame.Rect(3+x, 26+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.yellow, ski7)


        #legs Left
        leg2 = pygame.Rect(2+x, 22+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, leg2)
        leg3 = pygame.Rect(3+x, 23+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, leg3)
        leg4 = pygame.Rect(4+x, 24+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, leg4)

        #legs Right
        legR = pygame.Rect(10+x, 20+y, 3*size, 4*size)
        pygame.draw.rect(screen, color.blue, legR)
        legR1 = pygame.Rect(9+x, 20+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.blue, legR1)

        #skis Right
        skiR4 = pygame.Rect(10+x, 25+y, 3*size, 4*size)
        pygame.draw.rect(screen, color.black, skiR4)
        skiR5 = pygame.Rect(10+x, 29+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.black, skiR5)
        skiR6 = pygame.Rect(12+x, 29+y, 1*size, 1*size)
        pygame.draw.rect(screen, color.black, skiR6)
        skiR7 = pygame.Rect(11+x, 26+y, 1*size, 2*size)
        pygame.draw.rect(screen, color.yellow, skiR7)

        #legs Right
        legR2 = pygame.Rect(10+x, 24+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, legR2)
        legR3 = pygame.Rect(11+x, 23+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, legR3)
        legR4 = pygame.Rect(12+x, 22+y, 1*size, 3*size)
        pygame.draw.rect(screen, color.green, legR4)
        
        
        
        
        
        




        
