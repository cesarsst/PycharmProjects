# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar
# 0 termos

primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
pa = primeiro

c = 10
while c != -1:
    print('{} '.format(pa), end ='')
    pa += razao
    c -= 1
    if c == 0:
        c = int(input('\n Deseja mostrar mais quantos termos? [0]-Sair : '))
        if c == 0:
            c = -1