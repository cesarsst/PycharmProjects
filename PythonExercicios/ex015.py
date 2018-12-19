# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 por km rodado

km = float(input('Quantos Km forem percorridos?: '))
d = int(input('Quantos dias ele foi alugado?: '))

total = (d*60) + (km*0.15)
print('O valor total a ser pago para {} dias alugados e {}Km percorridos é de : R$:{}'.format(d, km, total))

