class Genero:
    def __init__(self):
        tipo_genero = ''

    def cadastrar_genero(self, tipo_genero):
        self.tipo_genero = tipo_genero

    def excluir_genero(self, tipo_genero):
        if self.tipo_genero == tipo_genero:
            self.tipo_genero = ''
