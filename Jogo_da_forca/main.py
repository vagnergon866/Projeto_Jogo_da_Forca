import jogo as j
import fileHandler as fileH

def mostrat_menu():
    print("=" * 30)
    print(" " * 7 + "JOGO DA FORCA")
    print("=" * 30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print("=" * 30)

arquivo = 'score.txt'
if fileH.existeArquivo(arquivo):
    print('Arquivo foi localizado no computador.')
else:
    print('Arquivo não existe.')
    fileH.criarArquivo(arquivo)

while True:
    mostrat_menu()
    opcao = int(input('Escolha a opção (1 - 2 - 3):'))

    if opcao == 1:
        print('Iniciar jogo!')
        j.jogar()
    elif opcao == 2:
        print('SCORE')
        dados = fileH.listarArquivo('score.txt')
        if not dados:
            print('Sore vazio.')
        else:
            i = 1
            for jogador in dados:
                print(f'{i} -> {jogador[0]}, Pontuação: {jogador[0][:-1]}')
                i += 1
    elif opcao == 3:
        print('Saindo do jogo. Até mais!')
        break
    else:
        print('Opção inválida, tente outra!')