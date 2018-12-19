#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas informações sobre ela (se é numero,alpha, alphanumerico)

msg = input('Digite algo:')
print('Só tem espaço: {}'.format(msg.isspace()))
print('O tipo digitado é: {}'.format(type(msg)))
print('O valor digitado é numerico? {}'.format(msg.isnumeric()))
print('O valor digitado é alfabetico? {}'.format(msg.isalpha()))
print('O valor digitado é alfanumerico? {}'.format(msg.isalnum()))
print('O valor digitado esta em maiusculo? {}'.format(msg.isupper()))
print('O valor digitado esta em minusculo? {}'.format(msg.islower()))
print('Esta capitalizada? {}'.format(msg.istitle()))    #Ex: Phyton
