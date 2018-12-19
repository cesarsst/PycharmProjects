# Escreva um programa que converta uma temperatura digitada em °c e converta para °f

temp = float(input('Digite a temperatura em °C:' ))
conv = (temp*(9/5))+32

print('A conversão de {}°C para °F é : {}°F'.format(temp, conv))
