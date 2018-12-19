# a confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# ate 9 ano = mirin
# ate 14 anos = infantil
# ate 19 anos = junior
# ate 20anos = senhor
# acima = master

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = (date.today().year) - ano

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Senior')
else:
    print('Categoria Master')