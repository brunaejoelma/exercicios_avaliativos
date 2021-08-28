from soma import Soma

vetor = [2, 5, 7]
#produto_total = Soma.soma(vetor)
soma_obj = Soma()

produto_total = soma_obj.soma(vetor)

print('O produto total do vetor é = ' + str(produto_total))
