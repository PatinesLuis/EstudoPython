def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta)) 
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo:')
    else:
        print('Arquivo {} for criado com suceso! \n' .format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo (nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo,'at')
    except:
        print('erro ao abrir o arquivo')
    else:
        a.write('{};{}\n' .format(nomeJogo, nomeVideogame))
    finally:
        a.close()

#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)


while True:
    print('MENU')
    print('1- CADASTRAR NOVO ITEM')
    print('2- LISTA CADASTRO')
    print('3- SAIR')

    op = valida_int('escolha a opção desejada: ',1,3)

    if op == 1 :
        print('OPÇÃO DE CADASTRAR NOVO ITEM SELECIONADA... \n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do VideoGame: ')
        cadastrarJogo(arquivo,nomeJogo, nomeVideogame)

    elif op == 2:
        print('OPÇÃO DE LISTA SELECIONADA... \n')
        listarArquivo(arquivo)

    elif op == 3:
        print('ENCERRANDO O PROGRAMA...')
        break