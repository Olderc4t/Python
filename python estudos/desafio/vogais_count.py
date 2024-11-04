"""
Escreva um programa que peça ao usuário para digitar uma frase e depois conte quantas vogais 
(a, e, i, o, u) há nessa frase. O programa deve exibir o total de vogais encontradas.
"""


palavra = input("Escreva uma frase!")
vogais = "AEIOUaeiou"
contador_vogal = 0

for vogal in palavra:
    if vogal in vogais:
        contador_vogal += 1

print(f'Temos {contador_vogal} vogais nessa frase!')