# faça um programa que leia um numero qualquer e mostre o seu fatorial

n = int(input('Digite um numero qualquer: '))
fat = n

while n != 1:
    fat *= (n - 1)
    n -= 1
print('O fatorial é: {} '.format(fat))