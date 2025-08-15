""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27 """

# Pergunta o usuário.
real = float(input('Quanto dinheiro você tem na carteira?R$ '))

# Faz o calculo.
dolar = real / 3.27

# Mostra o resultado.
print(f'Com \033[31mR${real:.2f}\033[m você pode comprar \033[32mUS${dolar:.2f}')