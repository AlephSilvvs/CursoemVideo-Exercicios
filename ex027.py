"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente. """

# Pergunta o nome, remove os espaços em branco
n = str(input('Digite seu nome completo: ')).strip()

# Fatia o nome e divide em espaços
nome = n.split()

# Mostra
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')  # O jeito mais facil de mostra o último nome é usando o -1