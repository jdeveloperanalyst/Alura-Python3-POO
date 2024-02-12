# Hora da prática: instância de uma classe

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

# Exercícios

# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

restaurante_praca.categoria = 'Italiana'
print(f'{restaurante_praca.categoria}')

# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_do_restaurante = restaurante_praca.nome
print(f'{nome_do_restaurante}')

# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

status = restaurante_praca.ativo
if status:
    print(f'O restaurante {nome_do_restaurante} está ATIVO!')
else:
    print(f'O restaurante {nome_do_restaurante} está INATIVO!')

# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

categoria = Restaurante.categoria

# 5. Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'

# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria é Fast Food!')
else:
    print(f'A categoria não é Fast Food!')

# 8. Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.ativo = True
print(f'restaurante_pizza.ativo atualizado para {restaurante_pizza.ativo}')

# 9. Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'{restaurante_praca.nome}, {restaurante_praca.categoria}')

