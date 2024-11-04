"""
Crie um jogo simples onde o computador escolhe um número aleatório entre 1 e 100,
 e o usuário tem que adivinhar qual é o número. O jogo deve dar dicas ao usuário se o palpite
 está muito alto ou muito baixo, e contar quantas tentativas o usuário fez até acertar.
"""
import random
numero_secreto = random.randint(1, 100)

numero_tentativas = 5

while numero_tentativas > 0:
    numero_user = int(input(f'diga um numero de 1 a 100! Mas cuidado pois so tem {numero_tentativas} tentativas'))

    numero_tentativas -=1
    

    if numero_user == numero_secreto :
        print('Parabens vc acertou!')
        break
    elif numero_user < numero_secreto:
        print('numero é maior!')
    elif numero_user > numero_secreto:
        print('O numero é menor!')

    if numero_tentativas == 0:
            print(f"não foi dessa vez o numero era {numero_secreto}, mas tente novamente!")

