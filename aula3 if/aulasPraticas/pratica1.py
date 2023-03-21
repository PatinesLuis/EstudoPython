x = int(input('Digite 1° valor: '))
y = int(input('Digite 2° valor: '))

print('QUAL OPERAÇÃO DESEJA REALIZAR COM OS 2 VALORES?')
print("+ adição")
print("- subtração")
print("* multiplicação")
print("/ divisão")

op = input('Digite o simbolo da operação: ')


if (op == '+'):
    calc = x + y
    print("A soma de {} e {} deu: {}" .format(x, y, calc))

elif(op == '-'):
    calc = x - y
    print("A subtração de {} e {} deu: {}" .format(x, y, calc))

elif(op == '*'):
    calc = x * y
    print("A Multiplicão de {} e {} deu: {}" .format(x, y, calc))

elif(op == '/'):
    calc = x / y
    print("A divisão de {} e {} deu: {}" .format(x, y, calc))

else:
    print('operador inexistente')


