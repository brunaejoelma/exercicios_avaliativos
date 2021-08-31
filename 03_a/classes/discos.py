from artista import Artista
from genero import Genero

class Discos:
    def __init__(self):
        titulo = ''
        artista = Artista()
        ano = 0
        genero = Genero()

    def cadastrar_disco(self, titulo, Artista, ano, Genero):
        self.titulo = titulo
        self.artista = Artista
        self.ano = ano
        self.genero = Genero

    def excluir_disco(self, titulo):
        if self.titulo == titulo:
            self.titulo = ''
            self.artista = Artista()
            self.ano = 0
            self.genero = Genero()
        else:
            print('Disco não encontrado.')

    def listar_discos(self):
        return 'Disco de título' + self.titulo + 'do ano: ' + str(self.Ano) + ', do genero' + self.Genero.tipo_genero + ', do artista' + self.Artista.nome
    def listar_disco_genero(self, Genero):
        if self.Genero.tipo_genero == Genero:
            return 'Disco de titulo: ' + self   ''.



