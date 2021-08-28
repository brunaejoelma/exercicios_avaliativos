from .conta_bancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self):
        super().__init__()

    def cadastrar_cp(self, nome, numero_conta, saldo):
        super.nome = nome
        super.numero_conta = numero_conta
        super.saldo = saldo

    def saque(self, valor, numero_conta):
        if numero_conta == super.numero_conta:
            if (valor - super.saldo) < 0:
                super.saldo = super.saldo - valor
            else:
                print('Saldo insuficiente.')
