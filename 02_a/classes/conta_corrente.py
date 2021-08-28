from .conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        super().__init__()
        self.limite_de_credito = 0.0

    def cadastrar_cc(self, nome, numero_conta, saldo):
        super().nome = nome
        super().numero_conta = numero_conta
        super().saldo = saldo

    def aumentar_limite(self, novo_limite):
        self.limite_de_credito = novo_limite

    def saque(self, valor, numero_conta):
        if numero_conta == super.numero_conta:
            if ((self.limite_de_credito + super.saldo) - valor) > 0:
                super.saldo = super.saldo - valor
            else:
                print('Saldo insuficiente.')

