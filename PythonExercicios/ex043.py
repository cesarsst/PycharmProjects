# Desenvolva uma logica que leia o peso e altura de uma pessoa,
# calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5 : abaixo do peso
# entre 18.5 e 25: peso ideal
# entre 25 a 30: sobrepeso
# entre 30 a 40: obesidade
# acima de 40 : obesidade morbida

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(pow(altura,2))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc <40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')

print('Seu IMC é de : {:.2f}'.format(imc))
