# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario
# se elas podem ou nao formar um triangulo

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if abs((r2-r3)) < r1 and (r2+r3) > r1:
    if abs((r1-r3)) < r2 and (r1+r3) > r2:
        if abs((r1-r2)) < r3 and (r1+r2) > r3:
            print('Pode formar triangulo!')
        else:
            print('Não podem formar triangulo')
    else:
        print('Não podem formar triangulo')
else:
    print('Não podem formar triangulo')


