# Desenvolva um programa que pergunte a distancia de uma viagem em Km
# Calcule o preço da passagem, cobrando 0,50 por km para viagens de até
# 200km e 0,45 para viagens mais longa

d = int(input('Digite quantos Km tem a viagem: '))

if d <= 200:
    p = d*0.5
else:
    p = d*0.45
print('O valor total a ser pago é de: R$:{}'.format(p))