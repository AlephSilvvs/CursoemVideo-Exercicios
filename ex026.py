"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

# Pede uma frase, deixa tudo maiusculo e remove os espaços em branco
frase = str(input('Digite uma frase: ')).upper().strip()

# Conta quanto 'A' tem na frase
print(f'A letra A aparece {frase.count('A')} vezes na frase.')

# Localiza a prinmeira letra 'A' na frase
print(f'A primeiroa letra A apareceu na posição {frase.find('A')+1}')

# Localiza a ultima letra 'A'
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}')