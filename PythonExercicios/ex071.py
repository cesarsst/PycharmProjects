# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o valor a ser sacado
#  e o programa vai informar quantas cedulas de cada valor serao entregues
# considere que o caixa possui cedulas de 50, 20, 10 e 1 real

valor = int(input('Digite o valor a ser sacado: '))

while True:
    ced50 = int(valor / 50)
    resto = valor % 50
    if resto == 0 :
        break
    ced20 = int(resto / 20)
    resto = resto % 20
    if resto == 0:
        break
    ced10 = int(resto / 10)
    resto = resto % 10
    if resto == 0:
        break
    ced1 = int(resto / 1)
    resto = resto % 1
    if resto == 0:
        break
print(f'Total de {ced50} cédulas de R$50:00')
print(f'Total de {ced20} cédulas de R$20:00')
print(f'Total de {ced10} cédulas de R$10:00')
print(f'Total de {ced1} cédulas de R$1:00')

# Outra forma:

valor = int(input('Que valor você quer sacar? R$: '))
total = valor
ced = 50
totaced = 0
while True:
    if total >= ced:
        total -= ced
        totaced += 1
    else:
        print(f'Total de {totaced} cédulas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaced = 0
        if total == 0:
            break