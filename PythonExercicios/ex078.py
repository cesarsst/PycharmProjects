# Faça um programa que leia 5 valores numericos e guarde em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista


menor = maior = 0
listamen = listamai = []

for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if menor == 0 == maior:
        menor = val
        maior = val
    if val < menor:
        listamen = []
        menor = val
        listamen.append(c)
    elif val > maior:
        listamai = []
        maior = val
        listamai.append(c)
    elif val == menor:
        listamen.append(c)
    elif val == maior:
        listamai.append(c)

print(f'Menor Valor: {menor} Posições: ', end='')
for c in range(0, len(listamen)):
    print(f'{listamen[c]}', end=' ')

print(f'\nMaior Valor: {maior} Posições:', end='')
for c in range(0, len(listamai)):
    print(f'{listamai[c]}', end=' ')