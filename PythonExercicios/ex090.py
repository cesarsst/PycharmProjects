# faça um programa que leia o nome e a média de um aluno, guardando também a situação
# em um dicionario. No final mostre o conteudo da estrutura na tela

situacao = {'Nome':'', 'Media':'', 'Situacao':''}

situacao['Nome'] = str(input('Digite o nome do aluno: '))
situacao['Media']= float(input('Digite a média do aluno: '))
if situacao['Media'] >= 7:
    situacao['Situacao'] = 'Aprovado'
else:
    situacao['Situacao'] = 'Reprovado'

for k, v in situacao.items():
    print(f'{k} é igual: {v}')

