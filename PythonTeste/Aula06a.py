#No input, o dado digitado é considerado uma string e não um numero
#Para ser considerado um numero, precisamos usar o tipo primitivo int()
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1+n2

print('A soma vale',s)
#outra forma de escrever o print: (mais poderosa)
print('A soma vale: {}!'.format(s))

# Quais são os tipos primitivos?
# int = 6,7,10
# float = 7.0, -15.45
# bool = True , False
# str = 'Olá', '7.5', ''
