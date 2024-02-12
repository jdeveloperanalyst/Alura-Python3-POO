"""
A condição elif
"""

print('*' * 32)
print('Bem vindo ao jogo de adivinhação')
print('*' * 32)

numero_secreto = 42

chute_str = input('Digite o seu número: ')

print('Você digitou o número: ', chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Você acertou')
else:
    if maior:
        print('Você errou! O seu chute foi maior que o número secreto ')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto ')

print('Fim do jogo')
