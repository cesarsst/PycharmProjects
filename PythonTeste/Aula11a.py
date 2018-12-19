# Cores no terminal

# \033[style text background m
# Ex: \033[0;33;44m
# Style: 0-none 1-negrito 4-sublinhado 7-inverte corers do fundo
# Text: 30 a 37 (cores)
# Back: 40 a 47 (cores de fundo)

print('\033[1;31;43mOlá, mundo \033[m')
nome = 'Cesar'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá, muito prazer em te conhecer, {}{}{} Stenico'.format('\033[4;34m', nome, '\033[m'))
print('Olá, muito prazer em te conhecer, {}{}{} Stenico'.format(cores['amarelo'], nome, cores['limpa']))