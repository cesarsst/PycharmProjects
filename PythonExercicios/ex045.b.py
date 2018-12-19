# Outra forma otimizada

from random import randint
from time import sleep

item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESSOURA """)
jogador = int(input('Qual é sua jogada? :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('-=' * 11)
print('Computador jogou: {}'.format(item[computador]))
print('Jogador jogou: {}'.format(item[jogador]))
print('-=' * 11)

if computador == 0:          #computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Você Perdeu!')
    else:
        print('Jogada Invalida!')
elif computador == 1:        #computador jogou papel
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada Invalida!')
elif computador == 2:        #computador jogou tessoura
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida!')