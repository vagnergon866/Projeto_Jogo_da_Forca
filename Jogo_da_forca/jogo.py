import fileHandler as fileH
import desenhos as d
from random import choice, random

def jogar():
    lista_palavras = list()
    arquivo = fileH.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo: #Lendo o arquivo e jogando para dentro da lista
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)

    for x in range(50):  # organizar a tela quando iniciar o jogo
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break

        # TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip()  # lower() vai deixar tudo em minusculo e o strip() vai ignorar alguma sujeira na digitação (espaço)
        if tentativa in digitadas:
            print('Você ja usou essa letra!')
            continue
        else:
            digitadas += tentativa  # ou pode usar o append()
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')

        score = d.desenhar_forca(erros)

        # CONSIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta é {palavra_sorteada}.')
            break

    fileH.incerirScore('score.txt', nome, score)