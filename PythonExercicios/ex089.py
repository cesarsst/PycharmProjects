# crie um programa que leia nome e duas notas de varios alunos
# e guarde tudo em uma lista composta. no final, mostre um boletim
# contendo a média de cada um e permita que o usuario possa mostrar
# as notas de cada aluno individulamente

lista = []
aluno = []
notas = []

while True:
    aluno.clear()
    notas.clear()

    aluno.append(str(input('Digite o nome do aluno: ')))
    n1 = float(input('Digite a nota 1: '))
    notas.append(n1)
    n2 = float(input('Digite a nota 2: '))
    notas.append(n2)
    aluno.append(notas[:])
    aluno.append((n1+n2)/2)
    lista.append(aluno[:])

    resp = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break

print('{:#^40}'.format('Boletim'))
print('{:<5} {:<10} {:>20}'.format('N°', 'Nome', 'Média'))
for i in range(0, len(lista)):
        print('{:<5} {:<10} {:>20}'.format(i, lista[i][0], lista[i][2]))

while True:
    num = int(input('Mostrar nota de qual aluno? [999 Interrompe] : '))
    if num == 999:
        break
    else:
        print(f'Notas de {lista[num][0]} são: {lista[num][1]}')