"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

# Dicionario de cores
cor = {'vermelho':'\033[31m',
       'verde':'\033[32m',
       'limpa':'\033[m'}

# Pergunta ao usuário
salario = float(input('Qual é o salário do funcionário? R$'))

# Condição
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

# Mostra na tela o resultado
print(f'Quem ganhava {cor['vermelho']}R${salario:.2f}{cor['limpa']} passa a ganhar {cor['verde']}R${novo:.2f}{cor['limpa']} agora.')