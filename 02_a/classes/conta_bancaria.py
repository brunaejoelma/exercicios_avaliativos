class ContaBancaria:
    def __init__(self):
        self.nome = ''
        self.numero_conta = ''
        self.saldo = 0.0

    def deposito(self, valor, numero_conta):
        if self.numero_conta == numero_conta:
            self.saldo = self.saldo + float(valor)
            print('Depósito efetuado com sucesso. Novo saldo = ' + str(self.saldo))

    def saque(self, valor, numero_conta):
        if self.numero_conta == numero_conta:
            self.saldo == self.saldo - valor
