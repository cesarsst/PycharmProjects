# Crie um programa onde o usuario possa digitar sete valores numericos
# e cadastre-os em uma lista unica que mantenha separados os
# valores pares e impares. no final mostre os valores pares e impares em ordem crescente

lista = [[], []]
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Valores Pares: {lista[0]} | Valores Impares: {lista[1]}')