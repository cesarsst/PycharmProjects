
from datetime import date

dados = {}

dados['nome'] = str(input('Digite o nome: '))
dados['ano_nasc'] = int(input('Digite o ano de nascimento: '))
dados['idade'] = date.today().year - dados['ano_nasc']
dados['ctps'] =  int(input('Digite a CTPS (0- Não tem): '))
if dados['ctps'] != 0:
    dados['ano_contr'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário'))
    dados['idade_ap'] = (dados['ano_contr'] + 35) - dados['ano_nasc']

for k, v in dados.items():
    print(f'{k} : {v}')
