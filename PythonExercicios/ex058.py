# Melhore o jogo do desafio 028 onde o computador vai pensar
# em um numero entre 0 a 10. só que o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessarios
# até vencer

from random import randint

comp = randint(1, 10)
tent = 0

palpite = int(input('Digite um numero: '))
tent += 1
while palpite != comp:
    if palpite < comp:
        palpite = int(input('Mais...Tente novamente: '))
        tent += 1
    elif palpite > comp:
        palpite = int(input('Menos...Tente novamente: '))
        tent += 1
print('Você acertou! Tentativas usadas: {}'.format(tent))


