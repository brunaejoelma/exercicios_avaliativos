from .artista import Artista
from .genero import Genero

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
        return 'Disco de título ' + self.titulo + ' do ano: ' + str(self.ano) + ', do genero ' + self.genero.tipo_genero + ', do artista ' + self.artista.nome

    def listar_disco_genero(self, tipo_genero):
        if self.Genero.tipo_genero == tipo_genero:
            return 'Disco de título' + self.titulo + 'do ano: ' + str(self.ano) + ', do genero' + self.Genero.tipo_genero + ', do artista' + self.Artista.nome

    def listar_disco_artista(self, nome_artista):
        if self.Artista.nome == nome_artista:
            return 'Disco de título' + self.titulo + 'do ano: ' + str(self.ano) + ', do genero' + self.Genero.tipo_genero + ', do artista' + self.Artista.nome




