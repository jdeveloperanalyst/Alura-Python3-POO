"""
Comparando tipos de dados de variáveis
"""

print('*' * 15)
print('Bem vindo ao jogo de adivinhação')
print('*' * 15)

number_secret = 42

chute_str = input('Digite o seu número: ')

print('Você digitou o número: ', chute_str)

chute = int(chute_str)

if number_secret == chute:
    print('Você acertou')
else:
    print('Você errou')
print('Fim do jogo')
