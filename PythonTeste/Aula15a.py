# Interrompendo repeticao while

cont = 1
while True:
    print(cont, '', end='')
    cont += 1
    if cont == 10:
        print(cont)
        break
print('Acabou')

# Ex 2:

s = num = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    s += num
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')           # outra forma de formatar variavies

# EX 3 - Modo de formatar string
nome = 'José'
idade = 33
salario = 999.3
print(f'O {nome} tem {idade} anos e ganha {salario:.2f}')