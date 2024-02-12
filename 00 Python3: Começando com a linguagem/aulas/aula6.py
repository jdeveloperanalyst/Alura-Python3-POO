# _Gerando números aleatórios_

import random


print('*' * 32)
print('Bem vindo ao jogo de adivinhação')
print('*' * 32, "\n")

numero_secreto = random.randrange(0, 101)
total_de_tentativa = 3

for rodada in range(1, total_de_tentativa + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativa))
    chute_str = input('Digite o seu número: ')
    print('Você digitou o número: {}'.format(chute_str))
    chute = int(chute_str)

    if chute < 1 or chute > 100:   # o operador lógico "or" é para interar em uma condição OU outra
        print("Você deve digitar um número entre 1 e 100!")
        continue  # a instrução continue não sai do loop apenas sai desta interação referente condição acima e volta ao começo do laço

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou.\n')
        break  # encerra o loop após acertar o número secreto --> "break" funciona com while tbm
    else:
        if maior:
            print('Você errou! O seu chute foi maior que o número secreto.\n')
        elif menor:
            print('Você errou! O seu chute foi menor que o número secreto.\n')

print('Fim do jogo!')
