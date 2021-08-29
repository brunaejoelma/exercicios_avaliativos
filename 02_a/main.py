from classes.conta_corrente import ContaCorrente
from classes.conta_poupanca import ContaPoupanca

continuar = True
while continuar:
    print('O que você deseja fazer? Digite:')
    print('[1] para cadastrar conta poupança')
    print('[2] para cadastrar conta corrente')
    print('[3] aumentar limite de conta corrente')
    print('[4] depósito em conta poupança')
    print('[5] depósito em conta corrente')
    print('[6] saque em conta poupança')
    print('[7] saque em conta corrente')
    valor_digitado = input(': ')

    if valor_digitado == '1':
        conta_poupanca = ContaPoupanca()
        conta_poupanca.cadastrar_cp(input('Informe o nome do titular: '), input('Informe o número da conta: '), 0.0)
        print('Conta cadastrada com sucesso')

    elif valor_digitado == '2':
        conta_corrente = ContaCorrente()
        conta_corrente.cadastrar_cc(input('Informe o nome do titular: '), input('Informe o número da conta: '), 0.0)
        print('Conta cadastrada com sucesso')

    elif valor_digitado == '3':
        conta_corrente.aumentar_limite(float(input('Informe o novo limite: ')))
        print('Limite alterado para:' + str(conta_corrente.limite_de_credito))

    elif valor_digitado == '4':
        conta_poupanca.deposito(input('Informe o valor do depósito: '), input('Informe o número da conta: '))

    elif valor_digitado == '5':
        conta_corrente.deposito(input('Informe o valor do depósito: '), input('Informe o número da conta: '))

    elif valor_digitado == '6':
        conta_poupanca.saque(float(input('Informe o valor a ser sacado: ')), input('Informe o número da conta:'))

    elif valor_digitado == '7':
        conta_corrente.saque(float(input('Informe o valor a ser sacado: ')), input('Informe o número da conta:'))

    verificacao = input('Digite 0 se deseja fazer outra operação: ' )

    if verificacao == '0':
        continue
    else:
        continuar = False
