# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e a condição de pagamento
# a vista: 10% de desconto
# cartao: 5%
# 2x cartao: preço normal
# 3x cartao: 20% de juros

print('{:=^40}'.format(' Lojas Stenicos '))
valor = float(input('Digite o valor do produto: '))
pag = int(input("""Qual metodo de pagemnto?
1 - Dinheiro/Cheque 
2- a vista cartão 
3- 2x no cartão 
4- 3x no cartão :"""))

if pag == 1:
    valor = valor - (valor * (10 / 100))
elif pag == 2:
    valor = valor - (valor * (5 / 100))
elif pag == 3:
    valor = valor
    print('O valor a ser pago será de {} em 2x de {}'.format(valor, valor / 2))
else:
    parc = int(input('Em quantas parcelas?: '))
    juros = (parc * (valor * (20 / 100)))
    valor = valor + juros
    print('Valor a ser pago pelo produto: {} | Total juros: {} '.format(valor, juros))
