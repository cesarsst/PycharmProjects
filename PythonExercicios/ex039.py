# Faça um programa que leia o oano de nascimento de uma jovem e
# informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também devera mostrar o tempo que falta ou passou do prazo

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = int(date.today().year) - ano

if idade < 18:
    print('Você ainda não tem idade para se alistar!')
    print('Falta {} anos!'.format(18-idade))
elif idade == 18:
    print('Está na hora de você se alistar!')
else:
    print('Você deveria ter se alistado à {} anos atras!'.format(idade-18))
