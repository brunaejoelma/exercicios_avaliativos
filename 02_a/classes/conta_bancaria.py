class ContaBancaria:
    def __init__(self):
        self.nome = ''
        self.numero_conta = ''
        self.saldo = 0.0

    def deposito(self, valor, numero_conta):
        if self.numero_conta == numero_conta:
            self.saldo = self.saldo + valor

    def saque(self, valor, numero_conta):
        if self.numero_conta == numero_conta:
            self.saldo == self.saldo - valor
