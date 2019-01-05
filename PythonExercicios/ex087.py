# Aprimore o ex 086 mostrando no final:
# a) a soma de todos os valores pares digitados
# b) a soma dos valores da terceira coluna
# c) o maior valor da segunda linha

lista = [[], [], []]
soma_par = 0

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Linha {i} Coluna {j}: '))
        lista[i].append(n)
        if n % 2 == 0:
            soma_par += n

for i in range(0, 3):
    for j in range(0, 3):
        print('|{0:^3}|'.format(lista[i][j]), end='  ')
    print('\n')

print(f'Soma de todos os valores pares: {soma_par}')

soma_3 = 0
for i in range (0, 3):
    soma_3 += lista[i][2]
print(f'A soma dos valores da terceira coluna é : {soma_3}')

maior = 0
for i in range(0, 3):
    if i == 0:
        maior = lista[1][i]
    else:
        if lista[1][i] > maior:
            maior = lista[1][i]
print(f'Maior valor da segunda linha: {maior}')