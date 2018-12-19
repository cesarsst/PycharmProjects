n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2

if m < 5:
    print('Você está abaixo da média!')
if m == 5:
    print('Você está na média!')
else:
    print('Você está acima da média!')
print('Sua nota foi: {}'.format(m))




