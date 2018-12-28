# Faça um programa que mostre a tabuada de varios numeros, um de cada
# vez, para cada valor digitado pelo usuario. O programa será interrompido
# quando o numero solicitado for negativo

n = 0
while n >= 0:
    n = int(input('Digite o valor para saber sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c:2}')
    print('{}'.format('=' * 20))