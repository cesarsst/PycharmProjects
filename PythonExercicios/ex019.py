# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
# ou podemos : from random import choice

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

aluno = [al1, al2, al3, al4]
sorteio = random.choice(aluno)              # uma escolha dentro da lista
print('O aluno sorteado foi o aluno {} !'.format(sorteio))




