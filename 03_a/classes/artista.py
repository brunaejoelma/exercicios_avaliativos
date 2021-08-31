
class Artista:
    def __init__(self):
        nome = ''

    def cadastrar_artista(self, nome):
        self.nome = nome
    def excluir_artista(self, nome):
          if self.nome == nome:
              self.nome = ''
          else:
              print('Artista não encontrado.')

