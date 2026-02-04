"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado"""


# Pergunta ao usuário
casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))


# Calcula a prestação e transforma anos em meses
prestacao = casa / (anos * 12)   # A pergunta das parcelas está em anos, mas o cálculo faz com meses


# Mostra a usuário
print (f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print (f' a prestação será de R${prestacao:.2f}')


# Condição simples
if prestacao <= 30 / 100 * salario:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Emprestimo NEGADO!')
