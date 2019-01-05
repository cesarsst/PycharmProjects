# Faça um programa que leia nome e peso de varias pessoas guardando
# tudo em uma lista. No final mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves

lista = []
galera = []
maior = menor = 0
while True:
    galera.append(str(input('Digite o nome: ')))
    galera.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        if galera[1] < menor:
            menor = galera[1]
    lista.append(galera[:])
    galera.clear()

    resp = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break


print(f' Pessoas cadastradas: {len(lista)}')
print(f'O maior peso foi {maior} , Peso de: ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {menor} , Peso de: ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end =' ')