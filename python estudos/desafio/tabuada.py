"""
peça ao usuário para digitar um número e, em seguida,
exiba a tabuada desse número (do 1 ao 10).
"""

primeiro_numero = int(input("Escreva um numero que deseje saber a tabuada!"))
multiplicador = 0

while multiplicador <= 10:
    multiplicação = primeiro_numero * multiplicador
    print(f'{primeiro_numero} X {multiplicador} = {multiplicação}')
    multiplicador += 1
