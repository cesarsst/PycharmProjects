# Faça um programa que ajude um jogador da mega sena a criar palpites
# o programa vai perguntar quantos jogos serao gerados e vai sortear
# 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta

from random import randint
jogos = []
jogadas = []

j = int(input('Quantos jogos serão feitos?: '))
for c in range(0, j):
    jogos.append(jogadas[:])

for i in range(0, j):
    for t in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in jogos[i]:
                jogos[i].append(n)
                break
    jogos[i].sort()

for c in range(0, j):
    print(f'Jogo {c+1}: {jogos[c]}')


