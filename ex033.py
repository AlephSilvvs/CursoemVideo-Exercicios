"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

# Pedindo os valores
a = input('Primeiro valor: ')
b = input('Segundo valor: ')
c = input('Terceiro valor: ')

# Verificando que é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Verificando que é o Maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

# Mostra na tela
print (f'O menor valor digitado foi {menor}')
print (f'O Maior valor digitado foi {maior}')