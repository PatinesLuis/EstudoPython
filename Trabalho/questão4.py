print('BEM VINDO AO CONTROLE DE FUNCIONARIOS DO LUIS EDUARDO PATINES !')
print('***************************************************************')

listaFuncionario = []
id_func = 0
def cadastrar_funcionario(id):
    print('----------- menu de cadastro de funcionarios -----------')

    print('Código do funcionario: {}' .format(id))
    nome = input('Entre com o nome: ')
    setor = input('Entre com o setor: ')
    salario = float(input('Entre com o salário: '))
    print('--------------*--------------------')

    dicionarioFuncionario = {'id':id,'nome':nome,'setor':setor,'salario':salario}
    listaFuncionario.append(dicionarioFuncionario.copy())


def consultar_funcionario():
    print('=== MENU DE CONSULTA DOS FUNCIONARIOS ===')
    print('Escolha a opção desejada')
    print('1- consultar todos os funcionarios:')
    print('2- consultar funcionarios por ID:')
    print('3- consultar funcionarios setor:')
    print('4- retornar:')

    op = int(input('>>'))

    if op == 1:
        print('----Você escolheu a opção consultar TODOS funcionarios----')
        print('-----------')
        for funcionario in listaFuncionario:
            for chave, valor in funcionario.items():    
                print('{}, {}' .format(chave,valor))
                print('-----------')

    if op == 2:
        print('----Você escolheu a opção consultar funcionarios por ID----')
        idEscolhido = int(input('Digite o código que deseja Buscar:'))
        print('Buscando...')
        for funcionario in listaFuncionario:
            if funcionario['id'] == idEscolhido:
                for chave, valor in funcionario.items():    
                    print('{}, {}' .format(chave,valor))
                    print('-----------')

    if op == 3:
        print('----Você escolheu a opção consultar funcionarios por SETOR----')
        idEscolhido = (input('Digite o SETOR que deseja Buscar:'))
        print('Buscando...')
        for funcionario in listaFuncionario:
            if funcionario['setor'] == idEscolhido:
                for chave, valor in funcionario.items():    
                    print('{}, {}' .format(chave,valor))
                    print('-----------')

    if op == 4:
        print('Saindo...')
        return

def remover_funcionario():
     print('----Você escolheu a opção REMOVER funcionario ----')
     idEscolhido = int(input('Digite o ID que deseja Buscar:'))
     print('Buscando...')
     for funcionario in listaFuncionario:
        if funcionario['id'] == idEscolhido:
            listaFuncionario.remove(funcionario)
            print('Funcionario removido\n')
#programa principal

while True:
    print('-------- MENU PRINCIPAL --------')
    print('Escolha a opção desejada')
    print('1- Cadastrar funcionarios')
    print('2- Consultar funcionário(s)')
    print('3- Remover funcionários')
    print('4-Sair')

    op = int(input('>>'))

    if op == 1:
        id_func = id_func +1
        cadastro = cadastrar_funcionario(id_func)
        continue
        
    elif op == 2:
        consulta = consultar_funcionario()
        continue

    elif op == 3:
        remover = remover_funcionario()
        continue

    elif op == 4:
        print('saindo...')
        break

    else:
        print('Digite uma opção valida')
        continue
