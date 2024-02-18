# Hora da prática: criando classes, construtores e métodos

# 1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    
    def __init__(self, titular='', saldo=0.0):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        
# 2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'{self._titular.ljust(15)} | R${str(self._saldo).ljust(15)} | {self.status}'

# 3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

# 4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
    @property
    def nome_titular(self):
        return self._titular
    
    @property
    def saldo_conta(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    @property
    def status(self):
        return '✅' if  self._ativo else '❌'

# 6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, cpf=0, nome='', idade=0, profissao='', telefone=''):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        self._telefone = telefone

# 7. Crie um método de classe para a conta ClienteBanco.
    @classmethod
    def criar_conta(cls, titular, saldo_incial):
        conta = ContaBancaria(titular, saldo_incial)
        return conta

#parte da etapa 2 do exercício
print()
conta1 = ContaBancaria("João", 1000.0)
conta2 = ContaBancaria("Maria", 500.0)
print(conta1)
print(conta2)

#parte da etapa 3 do exercício
print()
conta3 = ContaBancaria("Carlos", 200.0)
print(f"Antes de ativar a conta do {conta3._titular}:  Está ativa? {conta3.status}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar a conta do {conta3._titular}: Está ativa? {conta3.status}")
print()
print(conta3)

# 5. Crie uma instância da classe e imprima o valor da propriedade titular.
print()
conta4 = ContaBancaria('Pedro', 1500.0)
print(f'O nome do titular da conta 4 é {conta4.nome_titular}.')
print(conta4)

#parte da etapa 6 do exercício
cliente1 = ClienteBanco('12345678998', 'João', 31, 'Back End Developer', '11977448855')
cliente2 = ClienteBanco('32165498778', 'Maria', 25, 'Gerente de Projetos', '11999665544')
cliente3 = ClienteBanco('78932165445', 'Pedro', 31, 'Arquieteto', '11922447788')

#adicional da etapa 7 do exercício
print()
conta_cliente1 = ClienteBanco.criar_conta('Ana', 2000)
print(f'Conta de {conta_cliente1.nome_titular} criada com saldo inicial de R${conta_cliente1.saldo_conta}')
