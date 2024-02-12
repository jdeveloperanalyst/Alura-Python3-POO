# Hora da prática: condicionais

# Exercícios

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Escolha um número: '))
if numero % 2 == 0:
    print('O numero escolhido é PAR')
else:
    print('O numero escolhido é ÍMPAR')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input('Digite sua idade: '))
if 0 <= idade <= 12:
    # -> Criança: 0 a 12 anos;
    print('Categoria: Criança')
elif 13 <= idade <= 18:
    # -> Adolescente: 13 a 18 anos;
    print('Categoria: Adolescente')
else:
    # -> Adulto: acima de 18 anos.
    print('Categoria: Adulto')
    
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.    

nome_usuario = 'jonatas'
senha_usuario = 'senha123'

usuario = input('Insira o nome de usuário: ')
senha = input('Insira a senha: ')

if usuario == nome_usuario and senha == senha_usuario:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

x = int(input('Insira a coordenada de x: '))
y = int(input('Insira a coordenada de y: '))
if x > 0 and y > 0: 
    # -> Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    print('O ponto se encontra no "Primeiro Quadrante" do plano cartesiano.')
elif x < 0 and y > 0:
    # -> Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    print('O ponto se encontra no "Segundo Quadrante" do plano cartesiano.')
elif x < 0 and y < 0:
    # -> Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    print('O ponto se encontra no "Terceito Quadrante" do plano cartesiano.')
elif x > 0 and y < 0:
    # -> Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    print('O ponto se encontra no "Quarto Quadrante" do plano cartesiano.')
else:
    # -> Caso contrário: o ponto está localizado no eixo ou origem.
    print('O ponto está no "Eixo de Origem" do plano cartesiano.')
