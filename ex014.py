"""Escreva um porograma que converta uma temperatura
digitada em °C e converta para °F """

# Pergunta ao usuario
c = float(input('Informe a temperatura em °C: '))

# Faz o calculo e mostra na tela
f = 9 * c / 5 + 32
print(f'A temperatura de \033[31m{c}°C\033[m corresponde a \033[34m{f}°F\033[31m!')