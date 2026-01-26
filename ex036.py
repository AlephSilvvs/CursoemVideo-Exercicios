"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado"""

casa = int(input('Qual o valor da casa ? '))
salario = int(input('Qual o seu salário ? '))
anos = int(input('Quantas parcelas ? '))

prestacao = casa / (anos*12)   # A pergunta das parcelas está em anos, mas o cálculo faz com meses


if prestacao <= 30 / 100 * salario:
    print(f'Você terá que pagar R${prestacao:.2f} por mês durante {anos} anos')
else:
    print(f'Emprestimo negado')

