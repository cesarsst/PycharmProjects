# Escreve um programa que leia um ângulo qualquer e mostre na tela seu seno, cosseno e tangente

import math
num = int(input('Digite um angulo: '))
sen = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)

print('Seno: {} , Cos: {} e Tan: {}'.format(sen, cos,tan))
