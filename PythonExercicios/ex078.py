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

# outra forma
print('\n')

listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou os valores {listanum}')

print(f'Maior: {mai} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')

print(f'Menor: {men} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
