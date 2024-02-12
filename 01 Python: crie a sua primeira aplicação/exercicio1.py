# Hora da prática: a função print()

# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Exercício 1')
print('Python na Escola de Programação Alura.\n')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
print('Exercício 2')
nome = 'Jonatas'
idade = 31
print(f'Meu nome é {nome} e tenho {idade} anos.\n')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
print('Exercício 3')
print('A','L','U','R','A\n',sep='\n')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize: pi = 3.14159
print('Exercício 4')
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')
print(f'O valor arredondado de pi é: {round(pi, 2)}')
