# Condições

tempo = int(input('Quantos anos tem seu carro?: '))

if tempo <= 3:
    print('Seu carro está novo!')
else:
    print('Seu carro está velho!')
print('Fim!')

# Condição simplificada
print('carro novo' if tempo<=3 else 'carro velho')

# Ex 2

nome = str(input('Qual é seu nome?: '))

if nome == 'Cesar':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia {}'.format(nome))        # A indentação é importante nesse caso