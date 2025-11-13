"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

# Dicionario de cores
cor = {'limpa':'\033[m',
       'azul':'\033[1;49;34m',
       'vermelho1':'\033[1;31m',
       'amarelo':'\033[33m'}

# Pegunta ao usuário
velocidade = float(input('Qual é a velocidade do carro? '))

# Se a velocidade é maior que 80 é multado
if velocidade > 80:
    print(f'{cor['vermelho1']}MULTADO!{cor['limpa']} {cor['amarelo']}Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print (f'Você deve pagar uma multa de{cor['limpa']} {cor['vermelho1']}R${multa:.2f}{cor['limpa']}')

print(f'\n{cor['azul']}Tenha um bom dia! Dirija com segurança!{cor['limpa']}')