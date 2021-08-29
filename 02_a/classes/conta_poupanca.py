from .conta_bancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self):
        super().__init__()

    def cadastrar_cp(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def saque(self, valor, numero_conta):
        if numero_conta == self.numero_conta:
            if (self.saldo - valor) > 0:
                self.saldo = self.saldo - valor
                print('Saque efetuado com sucesso. Novo saldo = ' + str(self.saldo))
            else:
                print('Saldo insuficiente.')
