# Faça um programa que leia um numero inteiro e diga se ele é ou nao
# um numero primo

n = int(input('Digite um valor para verificar se é primo: '))
primo = 0

for c in range(1, n):
    if c != n and c != 1:
        if n % c == 0:
            primo = 1

if primo != 1:
    print('O numero é primo!')
else:
    print('O numero não é primo!')