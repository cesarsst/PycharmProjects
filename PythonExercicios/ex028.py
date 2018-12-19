# Escreva um programa que faça o computador 'pensar' em um numero inteiro
# entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido
# pelo computador . O programa deverá escrever na tela se o usuario venceu ou perdeu

from random import randint
n = randint(0, 5)
chute = int(input('Digite um valor entre 0 a 5 e tente acertar!: '))

if chute == n:
    print('Você acertou!')
else:
    print('Você errou!')
print('O valor correto era: {}'.format(n))

