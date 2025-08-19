"""Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

# Pergunta a largura e altura da parede
larg = float(input('Lagura da parede: '))
alt = float(input('Altura da parede: '))

# Calcula a altura e largura
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e a sua área é de {area}m²')

# Calcula a quantidade da tinta
tinta = area / 2
print (f'Para pintar essa parede, você precisará de {tinta}l de tinta')
