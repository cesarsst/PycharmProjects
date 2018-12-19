#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

ant = float(input('Qual o preço do produto? '))
des = ant - ((ant/100)*5)

print('O valor do produto com 5% de desconto é de R$:{}'.format(des))
