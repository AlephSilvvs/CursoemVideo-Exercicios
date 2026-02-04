"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado"""

# Pergunta ao usuario
casa = int(input('Qual o valor da casa: R$'))
salario = int(input('Qual o seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))

# Transforma anos em meses
prestacao = casa / (anos*12)   # A pergunta das parcelas está em anos, mas o cálculo faz com meses

# Condição simples
if prestacao <= 30 / 100 * salario:
    print(f'Você terá que pagar R${prestacao:.2f} por mês durante {anos} anos')
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Emprestimo negado')

