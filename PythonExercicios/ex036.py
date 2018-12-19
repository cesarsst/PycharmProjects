# Escreva um programa para aprovar um emprestimo bancario de uma casa
# O programa vai perguntar o valor da casa, o salario do comprador e
# em quantos anos ele vai pagar
# Calcule o valor da prestação mensal sabendo que ela nao pode execer
# 30% do salário ou então o emprestimo sera negado

pr_casa = float(input('Qual o valor da casa?:'))
sal = float(input('Qual o valor do salário?: '))
anos = int(input('Em quantos anos irá pagar?: '))

prestacao = pr_casa / (anos * 12)
min_pr = (30/100)*sal

print('Para pagar uma casa de R$:{} em {} anos a prestação será de R$:{:.2f}'.format(pr_casa, anos, prestacao))
if prestacao > min_pr:
    print('Emprestimo negado!')
else:
    print('Emprestimo autorizado!')
