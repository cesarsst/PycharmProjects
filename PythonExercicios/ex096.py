# Faça um programa que tenha uma função chamada area() que receba
# as dimensoes de um terreno retangular (largura e comprimento)
# e mostre a area do terreno

def area(lar, cmpr):
    a = lar * cmpr
    print(f'Área = {a:5.2f} m²')

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
