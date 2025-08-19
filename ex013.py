"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

# Pergunta o salario
salario = float(input('Qual é o salário?R$ '))

# Faz o calculo e mostra na tela
novo = salario + (salario * 15 / 100)
print (f'Um funcionário que ganhava \033[31mR${salario:.2f}\033[m,'
       f'\nCom 15% de aumento, passa a receber \033[34mR${novo:.2f}\033[m ')
