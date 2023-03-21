print('Bem-vindo ao programa de serviços de limpeza de Luis Eduardo Patines')
print('=====================================================================')

valorMetragem = 0
def metragem_limpeza():
    global valorMetragem
    while True:
        try: #tentar executar caso o usuario digite um valor número
            metragem = int(input('Entre com a metragem da casa: '))
        except ValueError: # caso o usuário não digite um valor númerico
            print('!! VALOR NÃO NÚMERICO')
            continue
    
        if metragem >= 30 and metragem <= 299:
            print('Será necessário(a) um(a) funcionario para a limpeza')
            valorMetragem = 60 + (0.3 * metragem)
            break
        elif metragem >= 300 and metragem <=699:
            print('Serão necessários(as) dois(duas) funcionários(as) para a limpeza')
            valorMetragem = 120 + (0.5 * metragem)
            break  
        else:
            print('!! NÃO aceitamos casas com metragem menor que 30m² ou Maior que 700m²')
            continue
    return metragem

multiplicador = 0
def tipo_limpeza():
    global multiplicador #puxando variável de fora da função
    while True:
        print('Entre com o tipo de limpeza')
        print('B - Básica - Indicada para sujeiras semanais ou quinzenais.')
        print('C - COMPLETA(30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras.')
        tipoLimpeza = input('').upper()
        if tipoLimpeza == 'B':
            print('Você selecionou a limpeza BÁSICA')
            multiplicador = 1
            break           
        elif tipoLimpeza == 'C':
            print('Você selecionou a limpeza Completa!')
            multiplicador = 1.30
            break
        else:
            print('OPÇÃO INVALIDA')
            continue
    return tipoLimpeza

valorAdicinal = 0
somaAdicional = 0   
def adicional_limpeza():

    while True:
        print('Deseja mais algum adicional?')
        print('0 - Não desejo mais nada (encerrar)')
        print('1 - Passar 10 peças de roupas - R$10,00')
        print('2 - Limpeza de 1 forno/microondas - R$12,00')
        print('3 - Limpeza de 1 geladeira/freezer - R$20,00')
        limpeza = int(input('>>'))

        global valorAdicinal
        global somaAdicional
        if limpeza == 1:
            valorAdicinal = 10
            somaAdicional += valorAdicinal
            continue
        elif limpeza == 2:
            valorAdicinal = 12
            somaAdicional += valorAdicinal
            continue
        elif limpeza == 3:
            valorAdicinal = 20
            somaAdicional += valorAdicinal
            continue

        elif limpeza == 0:
            print('Encerrando....')
            break
        else:
            print('nenhuma das opções digitadas')
            continue

#programa principal

print('========== menu 1 de 3 - metragem limpeza ==========')
metragem = metragem_limpeza()

print('\n========== menu 2 de 3 - Tipos de limpeza ==========')
tipoLimpeza = tipo_limpeza()


print('\n========== menu 3 de 3 - Tipos de limpeza ==========')
adicionallimpeza = adicional_limpeza()

soma = (valorMetragem * multiplicador) + somaAdicional

print('TOTAL: {} (metragem: {}.00 * tipo: {} + adicional: {}.00)' .format(soma, valorMetragem,  multiplicador, somaAdicional))
