"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado."""

# Pergunta ao usuario
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

# Faz o calculo e mostra
pago = (dias * 60) + (km * 0.15)
print(f'O total é de \033[34mR${pago:.2f}\033[m')