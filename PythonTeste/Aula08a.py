# Utilizando Modulos

# Teoria

# import bebida -> {cafe, refri, suco...}   importa toda biblioteca
# from bebida import cafe -> {cafe}         importa uma função da biblioteca

# Algumas bibliotecas : math (funcionalidades extras matematicas)

# Algumas funções da biblioteca math:
# ceil -> arredonda pra cima
# floor -> arredonda pra baixo
# trunc -> pega a parte inteira de um numero
# pow -> expoente
# sqrt -> raiz quadrada
# factorial -> fatorial

# Exemplo de chamada somente da função de raiz quadrada e ciel:
# from math import sqrt, ciel

# Pratica

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('Raiz quadrada de {} é: {}'.format(num, math.ceil(raiz)))     #arredonda a raiz pra cima (ciel)

#Segunda forma
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('Raiz quadrada de {} é: {}'.format(num, floor(raiz)))     #arredonda a raiz pra cima (ciel)


