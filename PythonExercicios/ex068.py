# faça um programa que jogue par ou impar com o computador.
# o jogo só sera interrompido quando o jogador perder, mostrando
# o total de vitorias consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep
count = 0
while True:
    # Escolhendo par ou impar
    while True:
        escolha = int(input('Digite [0]- para par [1]- para impar: '))
        if escolha == 0 or escolha == 1:
            break
    # Escolhendo valores para jogar
    n = int(input('Digite um valor: '))
    ncomp = randint(0, 10)
    print('Par....ou...impar..!')
    sleep(1)
    print(f'Você: {n} Computador: {ncomp}')

    # Verficando vitoria
    if ((n + ncomp) % 2) == 0 == escolha:
        print(f'Você Ganhou!')
        count += 1
    elif ((n + ncomp) % 2) != 0 and escolha != 0:
        print(f'Você Ganhou!')
        count += 1
    else:
        print(f'Você Perdeu!')
        break
    print('{}'.format('='*60))
print(f'Você ganhou {count}x sequidas!')

