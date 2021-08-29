from .conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        super().__init__()
        self.limite_de_credito = 0.0

    def cadastrar_cc(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def aumentar_limite(self, novo_limite):
        self.limite_de_credito = novo_limite

    def saque(self, valor, numero_conta):
        if numero_conta == self.numero_conta:
            if ((self.limite_de_credito + self.saldo) - valor) > 0:
                self.saldo = self.saldo - valor
                print('Saque efetuado com sucesso. Novo saldo = ' + str(self.saldo))
            else:
                print('Saldo insuficiente.')

