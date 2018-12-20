# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo desconsiderando os espaços

frase = str(input('Digite uma frase: ').lower())

# juntando todas palavras em uma string sem espaços
x = ''.join(frase.split())

# pegando o tamanho total da string nova
tam = len(x)

# variavel para verificar se é palindromo - 0- palindromo 1- n palindromo
palindromo = 0

d = tam-1                   # variavel auxiliar
for c in range(0, tam):
    if x[c] == x[d]:
        d -= 1
    else:
        print('Não é palindromo!')
        palindromo = 1
        break

# Verifica se é ou nao palindromo
if palindromo == 0:
    print('É palindromo!')










