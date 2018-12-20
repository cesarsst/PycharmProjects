# faça um programa que leia o peso de cinco pessoas.
# no final mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da pessoa: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso


print('Maior peso: {:2f}'.format(maior))
print('Menor peso: {:2f}'.format(menor))