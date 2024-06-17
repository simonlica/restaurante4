# Questão 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu sou {self.profissao}."

pessoa = Pessoa("Ana Clara", 28, "Médica")
print(pessoa)
pessoa.aniversario()
print(pessoa)
print(pessoa.saudacao)

# Questões 2, 3, 4 e 5
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

conta1 = ContaBancaria("Rafael Silva", 2000)
conta2 = ContaBancaria("Beatriz Costa", 3500)
print(conta1)
print(conta2)

conta = ContaBancaria("Paulo Roberto", 5000)
ContaBancaria.ativar_conta(conta)
print(conta.ativo)

# Questão 6
conta = ContaBancaria("Mariana Lima", 2500)
print(conta.titular)

# Questões 7 e 8
class ClienteBanco:
    def __init__(self, nome, idade, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @classmethod
    def criar_conta(cls, cliente, saldo_inicial):
        return ContaBancaria(cliente.nome, saldo_inicial)

cliente1 = ClienteBanco("Carlos Eduardo", 50, "Av. Paulista, 1000", "11987654321", "carlos.edu@example.com")
cliente2 = ClienteBanco("Fernanda Rocha", 35, "Rua das Flores, 200", "21987654321", "fernanda.rocha@example.com")
cliente3 = ClienteBanco("Lucas Andrade", 29, "Praça da Sé, 300", "31987654321", "lucas.andrade@example.com")

cliente = ClienteBanco("Mariana Lima", 29, "Rua das Palmeiras, 400", "41987654321", "mariana.lima@example.com")
conta = ClienteBanco.criar_conta(cliente, 3000)
print(conta)
