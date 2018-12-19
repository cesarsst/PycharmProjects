# Manipulando Texto em Python

frase = 'Curso em Video Python'

# Fatiamento
print(frase)
print(frase[9])                  # Pega a 9 letra da cadeia de caracteres da variavel frase
print(frase[9:14])               # Pega do 9 até o 14 (mas vai até o 13, para de conta do 14)
print(frase[9:21])               # Apesar de nao existir 21, ele pega só até o 20
print(frase[9:21:2])             # Pega do 9 ao 20 pulando de 2 em 2 espaços
print(frase[:5])                 # Pega do inicio até o valor 4 (5-1)
print(frase[15:])                # Pega do 15 até o final
print(frase[9::3])               # Pega do 9 até o final pulando de 3 em 3

# Análise
print(len(frase))                       # Mostra o comprimento da variavel
print(frase.count('o'))                 # Conta quantas vezes a letra 'o' está presente
print(frase.count('o',0,13))            # Contagem já com fatiamento entre o espaço 0 e 12
print(frase.find('deo'))                # Mostra a posição em que começou a string que procura
frase.find('Android')                   # Como não existe, retorna o valor -1
'Curso' in frase                        # Dentro da frase existe 'curso'? True or False


# Transformação
frase.replace('Python','Android')       # Substitui x por y
frase.upper()                           # Deixa tudo em maiusculo
frase.lower()                           # Deixa em minusculo
frase.capitalize()                      # Joga todos caracteres em minusculo, e só o primeiro fica em maiusculo
frase.title()                           # Analisa qts palavras existem, e faz um capitalize em todos
frase.strip()                           # Remove espaços inuteis no inicio e final da string
frase.rstrip()                          # Remove espaços inuteis somente do lado direito
frase.lstrip()                          # Remove espaços inuteis a esquerda

# Divisao
frase.split()                           # Onde tiver espaço, vai dividir em  outras string recebendo uma nova indexação, gera uma nova lista

# Junção
'-'.join(frase)                         # Junta todas as frases,antes separadas, separados por -
