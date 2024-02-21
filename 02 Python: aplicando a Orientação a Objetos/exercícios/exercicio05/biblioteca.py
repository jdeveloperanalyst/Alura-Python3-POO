from livro import Livro


if __name__ == '__main__':
    print()   
    print('Executei bibliteca.py') 
    print() 
    livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
    print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")
    livro_biblioteca.emprestar()
    print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")
    print()
    livro_biblioteca_1 = Livro("titulo testei", "Autor testei", 2023)
    Livro.livros = [livro_biblioteca_1]
    ano_especifico = 2023
    livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
    print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")
