# Crie um programa que crie uma matriz 3x3 e preencha com valores lidos
# pelo teclado
# no final, mostre a matriz na tela, com a formatação correta

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Linha {i} Coluna {j}: '))
        matriz[i].append(n)

for i in range(0, 3):
    for j in range(0, 3):
        print('|{0:^5}|'.format(matriz[i][j]), end='  ')
    print('\n')
