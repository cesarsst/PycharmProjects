# Crie um programa que tenha uma tupla unica com nomes de produtos
# e seus respectivos preços, na sequencia
# No final, mostre uma lsitagem de preços organizando os dados em forma tabular

lista = ('Pão', 1.50,
         'Frango', 10.00,
         'Leite', 3.50,
         'Batata', 1.50,
         'Refrigerante', 6.00)

print('{}\n{:^30}\n{}'.format('-'*30 , 'LISTAGEM DE PREÇOS', '-'*30))
for c in range(0, len(lista)):
    if c % 2 == 0:
      print(f'{lista[c]:.<20}', f'R$: {lista[c+1]:>5}')

print('{}'.format('-'*30))