# Crie um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9
# b) m que posição foi digitado o primiero valor 3
# c) Quais foram os numeros pares

tupla = ()

# Atribuindo valores a tupla
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    tupla = tupla + (n,)
print(tupla)
# item a
print(f'O número 9 apareceu {tupla.count(9)}')
# item b
if 3 in tupla:
    print(f'O numero 3 apareceu na  {(tupla.index(3) + 1)}° posição')
else:
    print('O numero 3 não apareceu nem uma vez!')
# item c
print('Numeros pares:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')