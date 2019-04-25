# Faça um programa que tenha uma função chama escreva() que receba
# um texto qualquer como parametro e mostre uma mensagem com
# tamanho adptavel


def escreva(txt):
    print(f'{"=" * len(txt)}')
    print(f'{txt}')
    print(f'{"=" * len(txt)}')
escreva('Hello, World!')
escreva('Curso Python - Cesar')