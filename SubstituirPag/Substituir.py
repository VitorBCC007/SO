#ATIVIDADE AULA 9 (SO)
from random import randint


def substituir_pag():  #NÃO ENCONTRADO SUBSTITUIR PÁGINA
    print('Substituir página')


matriz_100x5 = []  #MATRIZ DE PÁGINAS EM DISCO 
for cont in range(0, 100): #0 A 100
    n = cont  # N = COLUNA // CONTEM NÚMEROS DE 0 A 99 SEQUENCIAL
    i = cont + 1  # I = COLUNA i  TERÁ OS NÚMEROS DE 1 A 100 SEQUENCIAL 
    d = randint(1, 50)  # D = COLUNA // TERÁ NÚMEROS DE 1 A 50 (ALEATORIOS) 
    r = 0  # R = COLUNA / VALORES = 0 
    m = 0  # M = COLUNA / VALORES = 0
    matriz_100x5.append([n, i, d, r, m]) #FORMANDO MATRIZ UTILIZANDO DADOS  A CIMA
    print(matriz_100x5.__getitem__(cont))

print('*******************************')
print('-------------------------------')
print('*******************************')



matriz_10x5 = []  # MATRIZ DE MOLDURA DE PÁGINAS (RAM)
for cont in range(0, 10): #DE 0  A 10
    ind = randint(0, 99)  #SORTEANDO UM ÍNDICE DA MATRIZ 100X5  (matriz_100x5)
    matriz_10x5.append( #VALORES DA MATRIZ_10X5
        matriz_100x5.__getitem__(ind))  #ADICIONANDO A LINHA DA MATRIZ 100X5 REF AO ÍNDICE SORTEADO(matriz_10X5) 
    print(matriz_10x5.__getitem__(cont))

for c in range(0, 500): #0 ATÉ 500
    instrucao = randint(1,
                        100)  # NÚMERO 1 ATÉ 100, (CAMPO1) EXECUTADA NA CPU 
    esta_na_ram = False #ESTÁ NA RAM SERÁ FALSO
    for linha in matriz_10x5:  # VERIFICANDO CAMPO 1 (matriz_10x5) SE O VALOR ESTÁ CARREGANDO NA RAM
        if linha.__getitem__(1) == instrucao:  # SE ESTIVER
            linha.__setitem__(3, 1)  # O BIT R RECEBE 1
            chance_modif = randint(0, 100)  # A PÁGINA TERÁ 30% DE CHANCE DE SOFRER MODIFICAÇÃO
            if chance_modif <= 30:  # SE A PROBABILIDADE FOR ATINGIDA
                linha.__setitem__(2, linha.__getitem__(
                    2) + 1)  # O CAMPO (D) SERÁ ATUALIZADO (D = D + 1)
                linha.__setitem__(4, 1)  #O CAMPO MODIFICADO SERÁ ATUALIZADO M = 1
            esta_na_ram = True #SE ESTIVER NA RAM
            break #ENCERRAR
    if not esta_na_ram:  #CASO O NÚMERO DO SORTEIO NÃO ESTEJA NA MATRIZ 10X5
        substituir_pag()  # DEVE SER UTILIZADO A SUBSTITUIÇÃO DE PÁGINA 
        #SE NÃO FOR ENCONTRADO DEVE SUBSTITUIR POR ALGUM VALOR DA PÁGINA 
print('==============================')

for cont in range(0, 100): #MOSTRANDO MATRIZ 100X5
    print(matriz_100x5.__getitem__(cont))

print('==============================')

for cont in range(0, 10): #MOSTRANDO MATRIZ 10X5
    print(matriz_10x5.__getitem__(cont))

"""""
Para isso teremos 1 matriz com 10 linhas e 5 colunas para modelar as molduras de páginas na memória RAM e outra
 matriz 100 linhas e 5 colunas que vai representar as páginas em disco. Os campos da matriz são: 
 Número de Página (N), Instrução (I), Dado (D), Bit de Acesso (R), Bit de Modificação (M).
"""
