class UnidadeFederativa:
    @staticmethod
    def get_lista_uf():
        return ["Acre - AC", "Alagoas - AL", "Amapá - AP", "Amazonas - AM", "Bahia - BA", "Ceará - CE", "Distrito Federal - DF", "Espírito Santo - ES", "Goiás - GO", "Maranhão - MA", "Mato Grosso - MT", "Mato Grosso do Sul - MS", "Minas Gerais - MG", "Pará - PA", "Paraíba - PB", "Paraná - PR", "Pernambuco - PE", "Piauí - PI", "Rio de Janeiro - RJ", "Rio Grande do Norte - RN", "Rio Grande do Sul - RS", "Rondônia - RO", "Roraima - RR", "Santa Catarina - SC", "São Paulo - SP", "Sergipe - SE", "Tocantins -TO"]
    @staticmethod
    def get_uf(sigla):
        if sigla == 'AC':
            return 'Acre'
        elif sigla == 'AL':
            return 'Alagoas'
        elif sigla == 'AP':
            return  'Amapá'
        elif sigla == 'AM':
            return 'Amazonas'
        elif sigla == 'BA':
            return 'Bahia'
        elif sigla == 'CE':
            return 'Ceará'
        elif sigla == 'DF':
            return 'Distrito Federal'
        elif sigla == 'ES':
            return 'Espírito Santo'
        
