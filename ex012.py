"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

preço = float(input('Qual é o preço do produto?R$ '))

novo = preço - (preço * 5 / 100)

print (f'O produto que custava \033[31mR${preço:.2f}\033[m, '
       f'\nNa promoção com desconto de 5% vai custar \033[32mR${novo:.2f}\033[m')