
from datetime import date

dados = {
    'nome': '',
    'ano_nasc': '',
    'ctps': '',
    'ano_contr': '',
    'salario': '',
    'idade': '',
    'idade_ap': ''
}

dados['nome'] = str(input('Digite o nome: '))
dados['ano_nasc'] = int(input('Digite o ano de nascimento: '))
dados['ctps'] =  int(input('Digite a CTPS: '))
if dados['ctps'] != 0:
    dados['ano_contr'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário'))
    dados['idade_ap'] = (dados['ano_contr'] + 35) - dados['ano_nasc']
dados['idade'] = date.today().year - dados['ano_nasc']

for k, v in dados.items():
    print(f'{k} : {v}')
