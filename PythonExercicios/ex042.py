# Rafaça o desafio 035 dos triangulos acrescentando o recurso de
# mostrar que tipo de triangulo será formado
# eqilatero = todos os lados iquais
# isosceles = dois lados iguais
# escaleno = todos os lados diferente

a = float(input('Digite o lado 1: '))
b = float(input('Digite o lado 2: '))
c = float(input('Digite o lado 3: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Pode formar um triangulo!')
    if a == b and b == c:
        print('O triangulo é equilátero!')
    if a == b or b == c or c == a:
        print('O triangulo é isóceles!')
    else:
        print('Todos os lados diferentes!')
else:
    print('Não pode formar um triangulo!')

