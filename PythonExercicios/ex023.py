# Faça um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos digitos separados
# Ex> 1834 unidade = 4, dezena =3 centena =8 milhar =1

num = input('Digite um numero de 0 a 9999 : ')

und = num[3]
dez = num[2]
cen = num[1]
mil = num[0]

print(' \n Unidade = {} \n Dezena = {} \n Centena = {} \n Milhar = {}'.format(und, dez, cen, mil))
