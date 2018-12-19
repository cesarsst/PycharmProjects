# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

num = float(input('Digite um numero real: '))
r = trunc(num)

print('A parte inteira de {} é {}'.format(num, r))

