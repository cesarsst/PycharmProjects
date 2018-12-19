# Escreva um programa que leia um valor em metros e converta em centrimetros e milimetros

n = int(input('Digite o valor em metros: '))
cen = n * 100
mil = cen * 100

print('O valor em centrimetros é {} e em milimetros é {}'.format(cen, mil))
