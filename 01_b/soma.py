class Soma:
    @staticmethod
    def soma(vetor_valores):
        if (not isinstance(vetor_valores, list)):
            print('O parametro deve ser um vetor')
            return

        if (len(vetor_valores) < 1):
            print('O parametro deve ter pelo menos 1 valor')
            return

        produto_total = 0
        for valor in vetor_valores:
            produto_total = produto_total + valor

        return produto_total
