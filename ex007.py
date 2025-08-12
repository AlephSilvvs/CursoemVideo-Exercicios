"""Desenvolva um programa que leia as duas notas de um aluno,
cacule e mostre a sua média."""

# Pergunta as médias
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

# Calcula
m = (n1 + n2) / 2

# Mostra o resultado
print (f'\033[31mA média entre {n1:.1f} e {n2:.1f} é igual a {m:.1f}\033[m') # O ":.1f" faz aproximação, na soma das média 5.5 e 2 a resposta seria 3.75 mas foi aproximado para 3.8