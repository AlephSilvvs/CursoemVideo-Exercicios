"""Escreva um programa que leia um valor em metros e o exiba
convertido e mcontimetros e milimetros.""" #km hm dam m dm cm mm

# Pergunta a distância em metros
medida = float(input('Uma distância em metros: '))

# Faz as operações
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

# Mostra na tela
print(f'A medida de {medida}m coresponde a: \n{km:.0f}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')