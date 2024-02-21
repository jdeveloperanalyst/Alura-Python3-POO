from livro import Livro


def main():
    print()   
    print('Executei main.py') 
    print() 
    livro1 = Livro('teste', 'nomeTeste', 1992)
    livro2 = Livro('teste1', 'nomeTeste1', 2000)
    print(livro1)
    print(livro2)

if __name__ == '__main__':
    main()