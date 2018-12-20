# Desenvolva um programa que leia o primeiro termo e a razao de uma
# PA. No final, mostre os 10 primeiros termos dessa progressão

prTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    print('{}'.format(prTermo), end=' ')
    prTermo += razao