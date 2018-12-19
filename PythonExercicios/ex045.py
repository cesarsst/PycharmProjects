# Crie um programa que faça o computador jogar jokenpo com voce:

from random import randint
var = int(input('Escolha um:\n 1- Pedra\n 2- Papel\n 3- Tessoura\n:'))
comp = randint(1,3)

if var == comp:
    print('Empate!')
elif var == 1 and comp == 3:
    print('Você Ganhou! Voce:Pedra Computador: Tessoura')
elif var == 2 and comp == 1:
    print('Você Ganhou! Voce: Papel Computador: Pedra')
elif var == 3 and comp == 2:
    print('Voce Ganhou! Voce: Tessoura Computador: Papel')
else:
    if comp == 1:
        print('Voce perdeu! Você:Tessoura Computador: Pedra')
    elif comp == 2:
        print('Voce perdeu! Você: Pedra Computador: Papel ')
    else:
        print('Voce Perdeu! Voce: Papel Coputador: Tessoura')
