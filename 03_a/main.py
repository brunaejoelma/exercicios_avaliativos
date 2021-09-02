from classes.discos import Discos
from classes.artista import Artista
from classes.genero import Genero

continuar = True
while continuar:
    print('Informe o que deseja fazer:')
    print(' [ 01 ] Cadastrar Artista; \n [ 02 ] Excluir Artista; \n [ 03 ] Cadastrar Gênero; \n [ 04 ] Excluir Gênero; \n [ 05 ] Cadastrar Disco; \n [ 06 ] Excluir Disco; \n [ 07 ] Listar todos os discos; \n [ 08 ] Listar os discos de uma categoria; \n [ 09 ] Listar os discos de um artista')
    informado = input(': ')

    if informado == '01':
        artista = Artista()
        artista.cadastrar_artista(input('Informe nome do artista que deseja cadastrar: '))

    elif informado == '02':
        artista.excluir_artista(input('Informe o nome do artista que você deseja excluir: '))

    elif informado == '03':
        genero = Genero()
        genero.cadastrar_genero(input('Informe o nome do gênero que deseja cadastrar: '))

    elif informado == '04':
        genero.excluir_genero(input('Informe o nome do gênero que deseja excluir: '))

    elif informado == '05':
        disco = Discos()
        disco.cadastrar_disco(input('Digite o título do disco: '), artista, input('Informe o ano de lançamento do disco: '), genero)

    elif informado == '06':
        disco.excluir_disco(input('Informe o título do disco a ser excluído: '))

    elif informado == '07':
        print(disco.listar_discos())

    elif informado == '08':
        print(disco.listar_disco_genero(input('Informe a categoria a ser listada: ')))

    elif informado == '09':
        print(disco.listar_disco_artista(input('Informe o artista para que seja listados os discos: ')))

    verificar = input('Digite [ sim ] se deseja fazer outra operação: ')
    if verificar.lower() == 'sim':
        continuar = True
    else:
        continuar = False



