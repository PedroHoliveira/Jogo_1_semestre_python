#NOME DOS INTEGRANTES : Pedro Henrique de Oliveira, Guilherme Ariel Dos Santos Queiroz, Alexandre Gomes, Luiz Henrique Vieira Vicente


from ast import Del
from turtle import distance
from winreg import QueryInfoKey
import pygame
from pygame import *
from random import randint
import math
pygame.init()

altura = 600
largura = 800
tela = pygame.display.set_mode((largura, altura), 0, 32) 
pygame.display.set_caption("Jogo_Primeiro_Semestre")

#Texto
fonte = pygame.font.SysFont('arial', 40, True, False)

#MUSICA DENTRO DO JOGO
pygame.mixer.music.load('Música do Menu - Song.mp3')
pygame.mixer.music.play(-1)
volume = 0.010
pygame.mixer.music.set_volume(volume)

PI = math.acos(-1)  # define o valor de PI
TamTela = (800, 600)
xIni = TamTela[0] // 2
yIni = TamTela[1] // 2
Bolas = []

#JOGADOR
jogador_Img = []
p = pygame.image.load('Anjo de lado1-parte1.png')
jogador_Img.append(p)
p = pygame.image.load('Anjo de lado2.png')
jogador_Img.append(p)
p = pygame.image.load('Anjo de lado3.png')
jogador_Img.append(p)
p = pygame.image.load('Anjo de lado1-parte1.png')
jogador_Img.append(p)
i = 0.001

pontos = 0
jogador_Img = (pygame.image.load('Anjo de lado1-parte1.png'))
Jogador = pygame.transform.scale(jogador_Img,(60,100))
J2 = pygame.transform.flip(jogador_Img,True,False)
Jogador2 = pygame.transform.scale(J2,(60,100))
Esquerda = False
jogador_x = xIni
jogador_y = yIni
vida = 3
vida_img = pygame.image.load('Vida.png')
vida_img2 = pygame.image.load('Vida.png')
vida_img3 = pygame.image.load('Vida.png')
vel = 8

#INIMIGO 1
inimigo_Img = (pygame.image.load('Monster2.png'))
inimigo_x = 400
inimigo_y = 70
passo_X = 2
passo_Y = 2
RaioI = 40
Existe = True
MoveI = True
vida_inimigo = 5

inimigo_Img = []
todos = pygame.image.load('Monster2.png')
t = todos.subsurface([0, 0, 64, 64])
inimigo_Img.append(t)
t = todos.subsurface([64, 0, 64, 64])
inimigo_Img.append(t)
t = todos.subsurface([0, 64, 64, 64])
inimigo_Img.append(t)
t = todos.subsurface([64, 64, 64, 64])
inimigo_Img.append(t)
i = 0.001

#INIMIGO 2
inimigo_Img2 = (pygame.image.load('Monster2.png'))
inimigo_x2 = 70
inimigo_y2 = 100
passo_X2 = 2
passo_Y2 = 2
RaioI = 40
Existe2 = True
MoveI2 = True
vida_inimigo2 = 5

inimigo_Img2 = []
todos2 = pygame.image.load('Monster2.png')
t = todos2.subsurface([0, 0, 64, 64])
inimigo_Img2.append(t)
t = todos2.subsurface([64, 0, 64, 64])
inimigo_Img2.append(t)
t = todos2.subsurface([0, 64, 64, 64])
inimigo_Img2.append(t)
t = todos2.subsurface([64, 64, 64, 64])
inimigo_Img2.append(t)
i2 = 0.001

#INIMIGO 3
inimigo_Img3 = (pygame.image.load('Monster2.png'))
inimigo_x3 = 800-70
inimigo_y3 = 100
passo_X3 = 2
passo_Y3 = 2
RaioI = 40
Existe3 = True
MoveI3 = True
vida_inimigo3 = 5

inimigo_Img3 = []
todos3 = pygame.image.load('Monster2.png')
t = todos3.subsurface([0, 0, 64, 64])
inimigo_Img3.append(t)
t = todos3.subsurface([64, 0, 64, 64])
inimigo_Img3.append(t)
t = todos3.subsurface([0, 64, 64, 64])
inimigo_Img3.append(t)
t = todos3.subsurface([64, 64, 64, 64])
inimigo_Img3.append(t)
i3 = 0.001

#INIMIGO 4
inimigo_Img4 = (pygame.image.load('Monster2.png'))
inimigo_x4 = 400
inimigo_y4 = 600 - 70
passo_X4 = 2
passo_Y4 = 2
RaioI = 40
Existe4 = True
MoveI4 = True
vida_inimigo4 = 5

inimigo_Img4 = []
todos4 = pygame.image.load('Monster2.png')
t = todos4.subsurface([0, 0, 64, 64])
inimigo_Img4.append(t)
t = todos4.subsurface([64, 0, 64, 64])
inimigo_Img4.append(t)
t = todos4.subsurface([0, 64, 64, 64])
inimigo_Img4.append(t)
t = todos4.subsurface([64, 64, 64, 64])
inimigo_Img4.append(t)
i4 = 0.001

#INIMIGO 5
inimigo_Img5 = (pygame.image.load('Monster2.png'))
inimigo_x5 = 70
inimigo_y5 = 400
passo_X5 = 2
passo_Y5 = 2
RaioI = 40
Existe5 = True
MoveI5 = True
vida_inimigo5 = 5

inimigo_Img5 = []
todos5 = pygame.image.load('Monster2.png')
t = todos5.subsurface([0, 0, 64, 64])
inimigo_Img5.append(t)
t = todos5.subsurface([64, 0, 64, 64])
inimigo_Img5.append(t)
t = todos5.subsurface([0, 64, 64, 64])
inimigo_Img5.append(t)
t = todos5.subsurface([64, 64, 64, 64])
inimigo_Img5.append(t)
i5 = 0.001

#BOSS
inimigo_Img6 = (pygame.image.load('Monster2.png'))
inimigo_x6 = 70
inimigo_y6 = 400
passo_X6 = 2
passo_Y6 = 2
RaioI = 40
Existe6 = True
MoveI6 = True
vida_inimigo6 = 5

inimigo_Img6 = []
todos6 = pygame.image.load('Boss.png')
t = todos6.subsurface([0, 0, 60, 100])
inimigo_Img6.append(t)
t = todos6.subsurface([60, 0, 60, 100])
inimigo_Img6.append(t)
t = todos6.subsurface([120, 0, 60, 100])
inimigo_Img6.append(t)
t = todos6.subsurface([180, 0, 60, 100])
inimigo_Img6.append(t)
i6 = 0.001

#Inimigo 7
inimigo_Img7 = (pygame.image.load('Bat.png'))
inimigo_x7 = 400
inimigo_y7 = 150
passo_X7 = 2
passo_Y7 = 2
RaioI = 40
Existe7 = True
MoveI7 = True
vida_inimigo7 = 5

inimigo_Img7 = []
todos7 = pygame.image.load('Bat.png')
t = todos7.subsurface([0, 0, 64, 64])
inimigo_Img7.append(t)
t = todos7.subsurface([0, 64, 64, 64])
inimigo_Img7.append(t)
t = todos7.subsurface([0, 0, 64, 64])
inimigo_Img7.append(t)
t = todos7.subsurface([0, 64, 64, 64])
inimigo_Img7.append(t)
i7 = 0.001

#Inimigo 8
inimigo_Img8 = (pygame.image.load('Bat.png'))
inimigo_x8 = 450
inimigo_y8 = 150
passo_X8 = 2
passo_Y8 = 2
RaioI = 40
Existe8 = True
MoveI8 = True
vida_inimigo8 = 5

inimigo_Img8 = []
todos8 = pygame.image.load('Bat.png')
t = todos8.subsurface([0, 0, 64, 64])
inimigo_Img8.append(t)
t = todos8.subsurface([0, 64, 64, 64])
inimigo_Img8.append(t)
t = todos8.subsurface([0, 0, 64, 64])
inimigo_Img8.append(t)
t = todos8.subsurface([0, 64, 64, 64])
inimigo_Img8.append(t)
i8 = 0.001

#Inimigo 9
inimigo_Img9 = (pygame.image.load('Bat.png'))
inimigo_x9 = 400
inimigo_y9 = 150
passo_X9 = 2
passo_Y9 = 2
RaioI = 40
Existe9 = True
MoveI9 = True
vida_inimigo9 = 5

inimigo_Img9 = []
todos9 = pygame.image.load('Bat.png')
t = todos9.subsurface([0, 0, 64, 64])
inimigo_Img9.append(t)
t = todos9.subsurface([0, 64, 64, 64])
inimigo_Img9.append(t)
t = todos9.subsurface([0, 0, 64, 64])
inimigo_Img9.append(t)
t = todos9.subsurface([0, 64, 64, 64])
inimigo_Img9.append(t)
i9 = 0.001

Estado_Jogo = 0
# 0 - Menu
# 1 - JOGO
# 2 - GAMEOVER
# 3 - TELA BOSS
menu = pygame.image.load('Menu.png')
jogo = pygame.image.load('Nuvens_2.png')
gameover = pygame.image.load('Game Over.png')
tela_boss = pygame.image.load('Nuvens 1 .png')
xFundo = 0
tela2 = 0

def jogador(x, y):
    tela.blit(jogador_Img[int(i)], (jogador_x, jogador_y))

def inimigo(x, y):
    tela.blit(inimigo_Img[int(i)], (inimigo_x, inimigo_y))

def inimigo2(x, y):
    tela.blit(inimigo_Img2[int(i2)], (inimigo_x2, inimigo_y2))

def inimigo3(x, y):
    tela.blit(inimigo_Img3[int(i3)], (inimigo_x3, inimigo_y3))

def inimigo4(x, y):
    tela.blit(inimigo_Img4[int(i4)], (inimigo_x4, inimigo_y4))

def inimigo5(x, y):
    tela.blit(inimigo_Img5[int(i5)], (inimigo_x5, inimigo_y5))

def inimigo6(x, y):
    tela.blit(inimigo_Img6[int(i6)], (inimigo_x6, inimigo_y6))

def inimigo7(x, y):
    tela.blit(inimigo_Img7[int(i7)], (inimigo_x7, inimigo_y7))

def inimigo8(x, y):
    tela.blit(inimigo_Img8[int(i8)], (inimigo_x8, inimigo_y8))

def inimigo9(x, y):
    tela.blit(inimigo_Img9[int(i9)], (inimigo_x9, inimigo_y9))

def colidindo_projetil_inimigo (inimigo_x, inimigo_y, proj_x, proj_y):
    distancia = math.sqrt ((math.pow(inimigo_x-proj_x,2)) + (math.pow(inimigo_y-proj_y,2)))
    if distancia <= 64:
        return True
    else:
        return False

def NovaBola(posFinal):
    raio = 20
    cor = (0, 127, 255)
    xFim = posFinal[0]
    yFim = posFinal[1]
    distFim = ( (xFim - jogador_x)**2 + (yFim - jogador_y)**2 ) ** 0.5 # calcula a distância entre o centro da tela o o ponto clicado
    angulo = math.acos((xFim - jogador_x) / distFim) # calcula o ângulo da reta que passa peloo centro da tela e pelo ponto clicado
    if yFim > jogador_y:
        angulo = 2*PI - angulo # ajuste do ângulo para a parte inferior do quadro de desenho
    distAtual = 0 # variável a ser usada para o local efetivo do desenho da bolinha - começa no centro e vai até a posFinal
    passo = 4.1 # este passo define a velocidade da bolinha
    novabola = [posFinal, raio, cor, distFim, angulo, distAtual, passo, False]# especificações da bola
    Bolas.append(novabola)# adiciona as especificações da bola na lista

def DesenhaBolas(B):
    for i in range(len(B)):
        if B[i][5] <= B[i][3]:
            B[i][5] += B[i][6]
        else:
            B[i][7] = True
        X = jogador_x + int(B[i][5] * math.cos(B[i][4]))
        Y = jogador_y - int(B[i][5] * math.sin(B[i][4]))
        A = pygame.image.load('tiro2.png')
        A2 = pygame.transform.flip(A,True,False)
        Ataque = pygame.transform.scale(A,(50,50))
        Ataque2 = pygame.transform.scale(A2,(50,50))
        if (jogador_x > X):
            tela.blit(Ataque2, (X,Y) )
        elif (jogador_x < X):
            tela.blit(Ataque, (X,Y) )

def RemoveBolas(B):
    i = 0
    while i < len(B):
        if B[i][7]:
            del(B[i])
        else:
            i = i + 1

jogando = True
while jogando:

    pygame.mixer.music.load('Música do Menu - Song.mp3')
    pygame.mixer.music.play(-1)
    volume = 0.10
    pygame.mixer.music.set_volume(volume)

    while Estado_Jogo == 0:
        tela.blit(menu, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                jogando = False
        keys = pygame.key.get_pressed()
        if keys[K_s]:
            Estado_Jogo = 1

        vida = 3
        pontos = 0

        Existe = True
        MoveI = True
        vida_inimigo = 5
        passo_X = 3
        passo_Y = 3
        inimigo_x = 400
        inimigo_y = 70

        Existe2 = True
        MoveI2 = True
        vida_inimigo2 = 5
        passo_X2 = 3
        passo_Y2 = 3
        inimigo_x2 = 70
        inimigo_y2= 100

        Existe3 = True
        MoveI3 = True
        vida_inimigo3 = 5
        passo_X3 = 3
        passo_Y3 = 3
        inimigo_x3 = 800-70
        inimigo_y3 = 100

        Existe4 = True
        MoveI4 = True
        vida_inimigo4 = 5
        passo_X4 = 3
        passo_Y4 = 3
        inimigo_x4 = 400
        inimigo_y4 = 600-70

        Existe5 = True
        MoveI5 = True
        vida_inimigo5 = 5
        passo_X5 = 3
        passo_Y5 = 3
        inimigo_x5 = (randint(64,800-70))
        inimigo_y5= (randint(64,200))

        Existe6 = True
        MoveI6 = True
        vida_inimigo6 = 5
        passo_X6 = 5
        passo_Y6 = 5
        inimigo_x6 = 400
        inimigo_y6= 150

        Existe7 = True
        MoveI7 = True
        vida_inimigo7 = 5
        passo_X7 = 5
        passo_Y7 = 5
        inimigo_x7 = 70
        inimigo_y7= 400

        Existe8 = True
        MoveI8 = True
        vida_inimigo8 = 5
        passo_X8 = 5
        passo_Y8 = 5
        inimigo_x8 = 400
        inimigo_y8 = 70

        Existe9 = True
        MoveI9 = True
        vida_inimigo9 = 5
        passo_X9 = 5
        passo_Y9 = 5
        inimigo_x9 = 150
        inimigo_y9= 400

        pygame.display.update()

    while Estado_Jogo == 2:
        xFundo = xFundo -2
        largura_Fundo = tela.get_width()
        tela2 = (xFundo + largura_Fundo)
        if tela2 < 0:
            xFundo = 0
        tela.blit((gameover), (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                jogando = False
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            Estado_Jogo = 0

        mensagem = 'Pressione Espaço'
        texto_tela = fonte.render(mensagem, False, (255,255,255))
        tela.blit((texto_tela), (250, 500))
        pygame.display.update()
    
    while Estado_Jogo == 1:
        xFundo = xFundo -1
        largura_Fundo = tela.get_width()
        tela2 = (xFundo + largura_Fundo)
        if tela2 < 0:
            xFundo = 0
        tela.blit((jogo), (0,0))

        if vida == 3:
            tela.blit((vida_img), (0,0))
            tela.blit((vida_img2), (20,0))
            tela.blit((vida_img3), (40,0))
        if vida == 2:
            tela.blit((vida_img), (0,0))
            tela.blit((vida_img2), (20,0))
        if vida == 1:
            tela.blit((vida_img), (0,0))

        #MOVIMENTO
        keys = pygame.key.get_pressed() 

        if keys[pygame.K_a]:
            jogador_x -= vel
            Esquerda = True
                
        if keys[pygame.K_d]:
            jogador_x += vel
            Esquerda = False
            
        if keys[pygame.K_w]: 
            jogador_y -= vel

        if keys[pygame.K_s]: 
            jogador_y += vel 
        
        if not Esquerda:
            tela.blit(Jogador,(jogador_x, jogador_y-20))
        else:
            tela.blit(Jogador2, (jogador_x, jogador_y-20))
        i = i + 0.001
        if i > 3.999:
            i = 0

        #Colisão do Jogador na borda
        if jogador_x <= 0:
            jogador_x = 0
        elif jogador_x >= 800-64:
            jogador_x = 800-64

        if jogador_y <= -13:
            jogador_y = -13
        elif jogador_y >=600-100:
            jogador_y = 600-100

        #MOVIMENTO INIMIGO1
        if Existe:
            inimigo(inimigo_Img[int(i)], (inimigo_x, inimigo_y))
            i = i + 0.010
            if i > 3.999:
                i = 0
            if MoveI:
                inimigo_x = inimigo_x + passo_X
                if inimigo_x <= 0 or inimigo_x >= 800-64:
                    passo_X= -passo_X
                inimigo_y = inimigo_y + passo_Y
                if inimigo_y <= 0 or inimigo_y -1 >= 600-64:
                    passo_Y = -passo_Y
       
        #COLISÃO INIMIGO1 - PLAYER
        colisao_corpos = colidindo_projetil_inimigo(inimigo_x, inimigo_y, jogador_x, jogador_y)
        if colisao_corpos:
            vida -= 1
            if inimigo_x >= jogador_x or inimigo_x <= jogador_x:
                passo_X =- passo_X
                inimigo_x = 400
                inimigo_y = 70
            if inimigo_y >= jogador_y or inimigo_y <= jogador_y:
               passo_Y =- passo_Y
               inimigo_x = 400
               inimigo_y = 70
            print('-1 de vida{}' .format(vida))
        
        #Colisão com o Ataque INIMIGO 1
        for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
            raio = 12
            X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
            Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
            d = ( (inimigo_x - X) ** 2 + (inimigo_y - Y) ** 2) ** 0.5
            if (d <= RaioI + raio):
                inimigo_x = 400
                inimigo_y = 70
                vida_inimigo -= 1
                print(vida_inimigo)
                pontos += 10
                Existe = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                if vida_inimigo <= 0:
                    Existe = False
                    inimigo_x = (5000)
                    inimigo_y = (5000)
                    passo_X = 0
                    passo_Y = 0
                print('Colidiu {}' .format(pontos))
        
        #MOVIMENTO INIMIGO2
        if Existe2:
            inimigo2(inimigo_Img2[int(i2)], (inimigo_x2, inimigo_y2))
            i2 = i2 + 0.010
            if i2 > 3.999:
                i2 = 0
            if MoveI:
                inimigo_x2 = inimigo_x2 + passo_X2
                if inimigo_x2 <= 0 or inimigo_x2 >= 800-64:
                    passo_X2= -passo_X2
                inimigo_y2 = inimigo_y2 + passo_Y2
                if inimigo_y2 <= 0 or inimigo_y2 -1 >= 600-64:
                    passo_Y2 = -passo_Y2
        
        #COLISÃO INIMIGO2 - PLAYER
        colisao_corpos2 = colidindo_projetil_inimigo(inimigo_x2, inimigo_y2, jogador_x, jogador_y)
        if colisao_corpos2:
            vida -= 1
            if inimigo_x2 >= jogador_x or inimigo_x2 <= jogador_x:
                passo_X2 =- passo_X2
                inimigo_x2 = 70 
                inimigo_y2 = 100
            if inimigo_y2 >= jogador_y or inimigo_y2 <= jogador_y:
               passo_Y2 =- passo_Y2
               inimigo_x2 = 70
               inimigo_y2 = 100
            print('-1 de vida{}' .format(vida))
       
        #Colisão com o ataque INIMIGO 2
        for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
            raio = 12
            X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
            Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
            d = ( (inimigo_x2 - X) ** 2 + (inimigo_y2 - Y) ** 2) ** 0.5
            if (d <= RaioI + raio):
                inimigo_x2 = 70
                inimigo_y2 = 100
                vida_inimigo2 -= 1
                print(vida_inimigo2)
                pontos += 10
                Existe2 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                if vida_inimigo2 <= 0:
                    Existe2 = False
                    inimigo_x2 = (5000)
                    inimigo_y2 = (5000)
                    passo_X2 = 0
                    passo_Y2 = 0
                print('Colidiu {}' .format(pontos))

        #MOVIMENTO INIMIGO3
        if Existe3:
            inimigo3(inimigo_Img3[int(i3)], (inimigo_x3, inimigo_y3))
            i3 = i3 + 0.010
            if i3 > 3.999:
                i3 = 0
            if MoveI3:
                inimigo_x3 = inimigo_x3 + passo_X3
                if inimigo_x3 <= 0 or inimigo_x3 >= 800-64:
                    passo_X3 = -passo_X3
                inimigo_y3 = inimigo_y3 + passo_Y3
                if inimigo_y3 <= 0 or inimigo_y3 -1 >= 600-64:
                    passo_Y3 = -passo_Y3

        #COLISÃO INIMIGO3 - PLAYER
        colisao_corpos3 = colidindo_projetil_inimigo(inimigo_x3, inimigo_y3, jogador_x, jogador_y)
        if colisao_corpos3:
            vida -= 1
            if inimigo_x3 >= jogador_x or inimigo_x3 <= jogador_x:
                passo_X3 =- passo_X3
                inimigo_x3 = 800-70
                inimigo_y3 = 100
            if inimigo_y3 >= jogador_y or inimigo_y3 <= jogador_y:
               passo_Y3 =- passo_Y3
               inimigo_x3 = 800-70
               inimigo_y3 = 100
            print('-1 de vida{}' .format(vida))

        #Colisão com o ataque INIMIGO 3
        for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
            raio = 12
            X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
            Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
            d = ( (inimigo_x3 - X) ** 2 + (inimigo_y3 - Y) ** 2) ** 0.5
            if (d <= RaioI + raio):
                inimigo_x3 = 800-70
                inimigo_y3 = 100
                vida_inimigo3 -= 1
                print(vida_inimigo3)
                pontos += 10
                Existe3 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                if vida_inimigo3 <= 0:
                    Existe3 = False
                    inimigo_x3 = (5000)
                    inimigo_y3 = (5000)
                print('Colidiu {}' .format(pontos))

        #MOVIMENTO INIMIGO4
        if Existe4:
            inimigo4(inimigo_Img4[int(i4)], (inimigo_x4, inimigo_y4))
            i4 = i4 + 0.010
            if i4 > 3.999:
                i4 = 0
            if MoveI4:
                inimigo_x4 = inimigo_x4 + passo_X4
                if inimigo_x4 <= 0 or inimigo_x4 >= 800-64:
                    passo_X4 = -passo_X4
                inimigo_y4 = inimigo_y4 + passo_Y4
                if inimigo_y4 <= 0 or inimigo_y4 -1 >= 600-64:
                    passo_Y4 = -passo_Y4

        #Colisão inimigo4 - Player
        colisao_corpos4 = colidindo_projetil_inimigo(inimigo_x4, inimigo_y4, jogador_x, jogador_y)
        if colisao_corpos4:
            vida -= 1
            if inimigo_x4 >= jogador_x or inimigo_x4 <= jogador_x:
                passo_X4 =- passo_X4
                inimigo_x4 = 400
                inimigo_y4 = 600-70
            if inimigo_y4 >= jogador_y or inimigo_y4 <= jogador_y:
               passo_Y4 =- passo_Y4
               inimigo_x4 = (randint(64,800-70))
               inimigo_y4 = (randint(64,200))
            print('-1 de vida{}' .format(vida))

        #Colisão com o ataque INIMIGO 4
        for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
            raio = 12
            X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
            Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
            d = ( (inimigo_x4 - X) ** 2 + (inimigo_y4 - Y) ** 2) ** 0.5
            if (d <= RaioI + raio):
                inimigo_x4 = 400
                inimigo_y4 = 600-70
                vida_inimigo4 -= 1
                print(vida_inimigo4)
                pontos += 10
                Existe4 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                if vida_inimigo4 <= 0:
                    Existe4 = False
                    inimigo_x4 = (5000)
                    inimigo_y4 = (5000)
                print('Colidiu {}' .format(pontos))

        #MOVIMENTO INIMIGO5    
        if Existe5:
            inimigo5(inimigo_Img5[int(i5)], (inimigo_x5, inimigo_y5))
            i5 = i5 + 0.010
            if i5 > 3.999:
                i5 = 0
            if MoveI5:
                indimigo_x5 = inimigo_x5 + passo_X5
                if inimigo_x5 <= 0 or inimigo_x5 >= 800-64:
                    passo_X5 = -passo_X5
                inimigo_y5 = inimigo_y5 + passo_Y5
                if inimigo_y5 <= 0 or inimigo_y5 -1 >= 600-64:
                    passo_Y5 = -passo_Y5
        
        #Colisão inimigo5 - Player
        colisao_corpos5 = colidindo_projetil_inimigo(inimigo_x5, inimigo_y5, jogador_x, jogador_y)
        if colisao_corpos5:
            vida -= 1
            if inimigo_x5 >= jogador_x or inimigo_x5 <= jogador_x:
                passo_X5 =- passo_X5
                inimigo_x5 = (randint(64,800-64))
                inimigo_y5 = (randint(64,200))
            if inimigo_y5 >= jogador_y or inimigo_y5 <= jogador_y:
               passo_Y5 =- passo_Y5
               inimigo_x5 = (randint(64,800-64))
               inimigo_y5 = (randint(64,200))
            print('-1 de vida{}' .format(vida))
        
        #Colisão com o ataque INIMIGO 5
        for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
            raio = 12
            X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
            Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
            d = ( (inimigo_x5 - X) ** 2 + (inimigo_y5 - Y) ** 2) ** 0.5
            if (d <= RaioI + raio):
                inimigo_x5 = (randint(64,800-64))
                inimigo_y5 = (randint(64,200))
                vida_inimigo5 -= 1
                print(vida_inimigo5)
                pontos += 10
                Existe5 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                if vida_inimigo5 <= 0:
                    Existe5 = False
                    inimigo_x5 = (5000)
                    inimigo_y5 = (5000)
                print('Colidiu {}' .format(pontos))

        if pontos >= 250:
            #MOVIMENTO BOSS   
            if Existe6:
                inimigo6(inimigo_Img6[int(i6)], (inimigo_x6, inimigo_y6))
                i6 = i6 + 0.010
                if i6 > 3.999:
                    i6 = 0
                if MoveI6:
                    inimigo_x6 = inimigo_x6 + passo_X6
                    if inimigo_x6 <= 0 or inimigo_x6 >= 800-64:
                        passo_X6 = -passo_X6
                    inimigo_y6 = inimigo_y6 + passo_Y6
                    if inimigo_y6 <= 0 or inimigo_y6 -1 >= 600-64:
                        passo_Y6 = -passo_Y6
            
            #Colisão inimigo6 - Player
            colisao_corpos6 = colidindo_projetil_inimigo(inimigo_x6, inimigo_y6, jogador_x, jogador_y)
            if colisao_corpos6:
                vida -= 1
                if inimigo_x6 >= jogador_x or inimigo_x6 <= jogador_x:
                    passo_X6 =- passo_X6
                    inimigo_x6 = (randint(64,800-64))
                    inimigo_y6 = (randint(64,200))
                if inimigo_y6 >= jogador_y or inimigo_y6 <= jogador_y:
                    passo_Y6 =- passo_Y6
                    inimigo_x6 = (randint(64,800-64))
                    inimigo_y6 = (randint(64,200))
                print('-1 de vida{}' .format(vida))
            
            #Colisão com o ataque INIMIGO 6
            for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
                raio = 12
                X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
                Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
                d = ( (inimigo_x6 - X) ** 2 + (inimigo_y6 - Y) ** 2) ** 0.5
                if (d <= RaioI + raio):
                    inimigo_x6 = (randint(64,800-64))
                    inimigo_y6 = (randint(64,200))
                    vida_inimigo6 -= 1
                    print(vida_inimigo6)
                    pontos += 10
                    Existe6 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                    if vida_inimigo6 <= 0:
                        Existe6 = False
                        inimigo_x6 = (5000)
                        inimigo_y6 = (5000)
                        passo_X6 = 0
                        passo_Y6 = 0
                    print('Colidiu {}' .format(pontos))

            #MORCEGO
            if Existe7:
                inimigo7(inimigo_Img7[int(i7)], (inimigo_x7, inimigo_y7))
                i7 = i7 + 0.010
                if i7 > 3.999:
                    i7 = 0
                if MoveI7:
                    inimigo_x7 = inimigo_x7 + passo_X7
                    if inimigo_x7 <= 0 or inimigo_x7 >= 800-64:
                        passo_X7 = -passo_X7
                    inimigo_y7 = inimigo_y7 + passo_Y7
                    if inimigo_y7 <= 0 or inimigo_y7 -1 >= 600-64:
                        passo_Y7 = -passo_Y7            

            #Colisão inimigo7 - Player
            colisao_corpos7 = colidindo_projetil_inimigo(inimigo_x7, inimigo_y7, jogador_x, jogador_y)
            if colisao_corpos7:
                vida -= 1
                if inimigo_x7 >= jogador_x or inimigo_x7 <= jogador_x:
                    passo_X7 =- passo_X7
                    inimigo_x7 = (randint(64,800-64))
                    inimigo_y7 = (randint(64,200))
                if inimigo_y7 >= jogador_y or inimigo_y7 <= jogador_y:
                    passo_Y7 =- passo_Y7
                    inimigo_x7 = (randint(64,800-64))
                    inimigo_y7 = (randint(64,200))
                print('-1 de vida{}' .format(vida))
            
            for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
                raio = 12
                X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
                Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
                d = ( (inimigo_x7 - X) ** 2 + (inimigo_y7 - Y) ** 2) ** 0.5
                if (d <= RaioI + raio):
                    inimigo_x7 = (randint(64,800-64))
                    inimigo_y7 = (randint(64,200))
                    vida_inimigo7 -= 1
                    print(vida_inimigo7)
                    pontos += 10
                    Existe7 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                    if vida_inimigo7 <= 0:
                        Existe7 = False
                        inimigo_x7 = (5000)
                        inimigo_y7 = (5000)
                        passo_X7 = 0
                        passo_Y7 = 0
                    print('Colidiu {}' .format(pontos))


            #MORCEGO2
            if Existe8:
                inimigo8(inimigo_Img8[int(i8)], (inimigo_x8, inimigo_y8))
                i8 = i8 + 0.010
                if i8 > 3.999:
                    i8 = 0
                if MoveI8:
                    inimigo_x8 = inimigo_x8 + passo_X8
                    if inimigo_x8 <= 0 or inimigo_x8 >= 800-64:
                        passo_X8 = -passo_X8
                    inimigo_y8 = inimigo_y8 + passo_Y8
                    if inimigo_y8 <= 0 or inimigo_y8 -1 >= 600-64:
                        passo_Y8 = -passo_Y8            

            #Colisão inimigo8 - Player
            colisao_corpos8 = colidindo_projetil_inimigo(inimigo_x8, inimigo_y8, jogador_x, jogador_y)
            if colisao_corpos8:
                vida -= 1
                if inimigo_x8 >= jogador_x or inimigo_x8 <= jogador_x:
                    passo_X8 =- passo_X8
                    inimigo_x8 = (randint(64,800-64))
                    inimigo_y8 = (randint(64,200))
                if inimigo_y8 >= jogador_y or inimigo_y8 <= jogador_y:
                    passo_Y8 =- passo_Y8
                    inimigo_x8 = (randint(64,800-64))
                    inimigo_y8 = (randint(64,200))
                print('-1 de vida{}' .format(vida))
            
             #Colisão com o ataque INIMIGO 8
            for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
                raio = 12
                X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
                Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
                d = ( (inimigo_x8 - X) ** 2 + (inimigo_y8 - Y) ** 2) ** 0.5
                if (d <= RaioI + raio):
                    inimigo_x8 = (randint(64,800-64))
                    inimigo_y8 = (randint(64,200))
                    vida_inimigo8 -= 1
                    print(vida_inimigo8)
                    pontos += 10
                    Existe8 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                    if vida_inimigo8 <= 0:
                        Existe8 = False
                        inimigo_x8 = (5000)
                        inimigo_y8 = (5000)
                        passo_X8 = 0
                        passo_Y8 = 0
                    print('Colidiu {}' .format(pontos))

            #MORCEGO3
            if Existe9:
                inimigo9(inimigo_Img9[int(i9)], (inimigo_x9, inimigo_y9))
                i9 = i9 + 0.010
                if i9 > 3.999:
                    i9 = 0
                if MoveI9:
                    inimigo_x9 = inimigo_x9 + passo_X9
                    if inimigo_x9 <= 0 or inimigo_x9 >= 800-64:
                        passo_X9 = -passo_X9
                    inimigo_y9 = inimigo_y9 + passo_Y9
                    if inimigo_y9 <= 0 or inimigo_y9 -1 >= 600-64:
                        passo_Y9 = -passo_Y9            

            #Colisão inimigo9 - Player
            colisao_corpos9 = colidindo_projetil_inimigo(inimigo_x9, inimigo_y9, jogador_x, jogador_y)
            if colisao_corpos9:
                vida -= 1
                if inimigo_x9 >= jogador_x or inimigo_x9 <= jogador_x:
                    passo_X9 =- passo_X9
                    inimigo_x9 = (randint(64,800-64))
                    inimigo_y9 = (randint(64,200))
                if inimigo_y9 >= jogador_y or inimigo_y9 <= jogador_y:
                    passo_Y9 =- passo_Y9
                    inimigo_x9 = (randint(64,800-64))
                    inimigo_y9 = (randint(64,200))
                print('-1 de vida{}' .format(vida))
            
             #Colisão com o ataque INIMIGO 8
            for i in range(len(Bolas)):# confere se os inimigos colidiram com o ataque do personagem
                raio = 12
                X = jogador_x + int(Bolas[i][5] * math.cos(Bolas[i][4]))
                Y = jogador_y - int(Bolas[i][5] * math.sin(Bolas[i][4]))
                d = ( (inimigo_x9 - X) ** 2 + (inimigo_y9 - Y) ** 2) ** 0.5
                if (d <= RaioI + raio):
                    inimigo_x9 = (randint(64,800-64))
                    inimigo_y9 = (randint(64,200))
                    vida_inimigo9 -= 1
                    print(vida_inimigo9)
                    pontos += 10
                    Existe8 = True # ADICIONAR CONTADOR PARA VIDA NO INIMIGO EXISTE = TRUE
                    if vida_inimigo9 <= 0:
                        Existe9 = False
                        inimigo_x9 = (5000)
                        inimigo_y9 = (5000)
                        passo_X9 = 0
                        passo_Y9 = 0
                    print('Colidiu {}' .format(pontos))

        if pontos == 420:
            Estado_Jogo = 0

        RemoveBolas(Bolas)
        DesenhaBolas(Bolas)
        #GAMEOVER
        if vida <= 0:
            Estado_Jogo = 2

        for evento in pygame.event.get():
            if evento.type == QUIT:        
                jogando = False
            elif evento.type == MOUSEBUTTONDOWN:
                botoesMouse = pygame.mouse.get_pressed()
            elif evento.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if botoesMouse[0]:
                    NovaBola(pos)
    
        pygame.display.update()

pygame.quit()