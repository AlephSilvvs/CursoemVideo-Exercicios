"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido"""

# Importa biblioteca, somente a função choice, pois não usaremos outras funções no momento
from random import choice

# Pergunta os nomes
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Lista e randomizando os nomes
lista = [n2,n2,n3,n4]
escolhido = choice(lista) # Como só foi importado a função "choice" não precisa fazer referência a "math"
print(f'O aluno escolhido foi{escolhido}')



""" Melhor forma de fazer esse execício


import random

# Lista para armazenar os nomes
nomes = []

# Loop para ler os nomes
print("Digite os nomes que você quer sortear. Digite 'fim' quando terminar.")
while True:
    nome = input("Digite um nome: ")
    if nome.lower() == 'fim':
        break  # Sai do loop se o usuário digitar 'fim'
    elif nome:  # Garante que não adicionamos nomes vazios
        nomes.append(nome)

# Verifica se a lista não está vazia antes de sortear
if nomes:
    # Sorteia um nome da lista
    nome_sorteado = random.choice(nomes)

    # Exibe o nome sorteado
    print(f"\nO nome sorteado foi: {nome_sorteado}")
else:
    print("\nNenhum nome foi digitado. O sorteio não pode ser realizado.") """