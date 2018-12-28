# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
# Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

numeros = ()

for c in range(0, 5):
    n = randint(0, 10)
    numeros = numeros + (n,)

print(numeros)

menor = maior = 0
for c in range(0, 5):
    if maior == menor == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        elif numeros[c] < menor:
            menor = numeros[c]
print(f'Maior Valor {maior}, Menor Valor {menor}')

# outra forma de mostrar o maior e menor nas tuplas
print(f'O maior valor sorteado foi {max(numeros)} e o menor {min(numeros)}')