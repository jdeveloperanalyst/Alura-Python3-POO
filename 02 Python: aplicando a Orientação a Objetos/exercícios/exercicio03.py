#Classe 'Musica' com os atributos 'nome', 'artista' e 'duracao'
class Musica:
    lista_de_musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.lista_de_musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musica():
        for musica in Musica.lista_de_musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
            
        
musica1 = Musica('Veneno','Leo Stronda', 192)
musica2 = Musica('Aulas e Cursos', 'DNASTY', 199)
musica3 = Musica('Mustang Preto', 'Teto', 181)

Musica.listar_musica()


# class Musica:
#     def __init__(self, nome='', artista='', duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
# musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
# musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

#Hora da prática: métodos especiais e atributos

#Exercícios

# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo='Honda HRV', cor='Cinza Chumbo', ano=2016)  

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, localizacao , capacidade=0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.localizacao = localizacao
        self.capacidade = capacidade
        self.ativo = ativo

restaurante1 = Restaurante(nome='Pizza Hut', categoria='Italiana', localizacao='Rua: Ari Não To Nem Ai', capacidade=60, ativo=True)  

# 3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    
    localizacao = 'São Paulo'
    capacidade = 65
        
restaurante2 = Restaurante(nome='Mania de Churrasco', categoria='Carne')

# 4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        
    localizacao = 'São Paulo'
    capacidade = 65
        
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'
        
restaurante3 = Restaurante(nome='Mania de Churrasco', categoria='Carne')

print(restaurante3)

# 5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Clientes:
    clientes = []
    def __init__(self, nome, email, telefone, endereço):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereço = endereço
        Clientes.clientes.append(self)
        
    def listar_clientes():
        for cliente in Clientes.clientes:
            print(f'{cliente.nome} | {cliente.email} | {cliente.telefone} | {cliente.endereço}')
            
cliente1 = Clientes(nome='Jon', email='jonwick@hotmail.com', telefone='11-111111111', endereço='Rua: bla bla blu blu')
cliente2 = Clientes(nome='Jonas', email='jonas@hotmail.com', telefone='22-222222222', endereço='Rua: blu blu bla bla')
cliente3 = Clientes(nome='Joninhas', email='joninhas@hotmail.com', telefone='33-333333333', endereço='Rua: bla blu bla blu')

Clientes.listar_clientes()
