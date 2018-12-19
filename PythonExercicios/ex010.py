#Crie um programa que leia quanto dinheiro uma pesso tem na carteira e quanto dolares ela pode comprar - tome 1 dolar como 3,27

n = float(input('Quanto reais tem na carteira? '))
r = n // 3.27
print('Com {} você pode comprar {} dolares'.format(n, r))

