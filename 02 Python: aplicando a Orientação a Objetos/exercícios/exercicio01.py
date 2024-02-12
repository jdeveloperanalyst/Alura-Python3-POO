# Mão na massa: classe música

'''
Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. 
Um objeto é uma instância específica de uma classe, e as classes são utilizadas para 
definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos
(que trazem as características ou propriedades de um objeto):

nome
artista
duracao
'''

# 1 - Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..

#Classe 'Musica' com os atributos 'nome', 'artista' e 'duracao'
class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Veneno'
musica1.artista = 'Leo Stronda'
musica1.duracao = 192

musica2 = Musica()
musica2.nome = 'Aulas e Cursos'
musica2.artista = 'DNASTY'
musica2.duracao = 199

musica3 = Musica()
musica3.nome = 'Mustang Preto'
musica3.artista = 'Teto'
musica3.duracao = 181

print(vars(musica1))
print(vars(musica2))
print(vars(musica3))