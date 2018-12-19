# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e a condição de pagamento
# a vista: 10% de desconto
# cartao: 5%
# 2x cartao: preço normal
# 3x cartao: 20% de juros

valor = float(input('Digite o valor do produto: '))
pag = int(input('Qual metodo de pagemnto?\n 1 - Dinheiro/Cheque \n '
      '2-Cartão \n 3- 2x no cartão \n 4- 3x no cartão \n :'))

if pag == 1:
    valor = valor-(valor*(10/100))
elif pag == 2:
    valor = valor-(valor*(5/100))
elif pag == 3:
    valor = valor
else:
    valor = valor+(valor*(20/100))
print('Valor a ser pago pelo produto: {}'.format(valor))
