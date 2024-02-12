"""
O laço com while
"""

print('*' * 32)
print('Bem vindo ao jogo de adivinhação')
print('*' * 32, "\n")

numero_secreto = 42
total_de_tentativa = 3
rodada = 1

while rodada <= total_de_tentativa:
    print("Tentativa {} de {}".format(rodada, total_de_tentativa))
    chute_str = input('Digite o seu número: ')
    print('Você digitou o número: {}'.format(chute_str))
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou.\n')
    else:
        if maior:
            print('Você errou! O seu chute foi maior que o número secreto.\n')
        elif menor:
            print('Você errou! O seu chute foi menor que o número secreto.\n')
            
    rodada += 1

print('Fim do jogo!')
