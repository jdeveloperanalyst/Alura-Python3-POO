class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        
    def __str__(self):
        return f'{self._titulo.ljust(25)} | {self._autor.ljust(25)} | {str(self._ano_publicacao).ljust(25)}'
    
    def emprestar(self):
        self._disponivel = False
        
    @staticmethod    
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

print()        
livro1 = Livro('O Senhor dos Anéis', 'J. R. R. Tolkien', 1954)
livro2 = Livro('1984', 'George Orwell', 1949)
print(livro1)
print(livro2)
print()

livro3 = Livro('Cem Anos de Solidão', 'Gabriel García Márquez', 1967)
print(f'Antes de emprestar o livro3: Livro disponível? {livro3._disponivel}')
livro3.emprestar()
print(f'Depois de emprestar o livro3: Livro disponível? {livro3._disponivel}')

Livro.livros = [livro1, livro2, livro3]