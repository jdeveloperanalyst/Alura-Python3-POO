# Hora da prática: listas, for e try except

# Exercícios
# 1 - Crie uma lista para cada informação a seguir:

# -> Lista de números de 1 a 10;

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -> Lista com quatro nomes;

lista_de_nomes = ['Jonatas', 'Carla', 'Socorro', 'Carlos']

# -> Lista com o ano que você nasceu e o ano atual.

lista_de_ano = [1992, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for nome in lista_de_nomes:
    print(f'.{nome}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# soma = 0
# for numero in range(1, 11):
#     print(numero)
#     if numero % 2 == 1:
#         soma += numero
# print(f'A soma dos números ímpares são: {soma}')
    
soma_impares = 0
for numero in range(1, 11, 2):
    print(numero)
    soma_impares += numero
print(f'A soma dos números ímpares são: {soma_impares}')
    
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for numero in range(10, 0, -1):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
 
escolha_um_numero = int(input('Digite um número: '))
for numero in range(1, 11):
    multiplica = numero * escolha_um_numero
    print(f'{escolha_um_numero:2d} x {numero:2d} = {multiplica:2d}')
 
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_de_numeros = [10, 20, 30, 40]
soma = 0
try:
    for numero in lista_de_numeros:
        soma += numero
    print(soma)
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_de_numeros = [10, 20, 30, 40]
soma = 0
try:
    for numero in lista_de_numeros:
        soma += numero
    media = soma / len(lista_de_numeros)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f'Ocorreu um erro: {e}')
