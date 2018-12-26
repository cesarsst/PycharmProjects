# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo desconsiderando os espaços

frase = str(input('Digite uma frase: ').lower())

# juntando todas palavras em uma string sem espaços
x = ''.join(frase.split())

# pegando o tamanho total da string nova
tam = len(x)

# 1 solução para inter:
inverso = x[::-1]

# 2 solução
#inverso = ''
#for letra in range(tam-1, -1, -1):
#    inverso += x[letra]

if inverso == x:
    print('É palindromo! ')
else:
    print('Não é palindromo!')












