#solicita entrada ao usuario
try:
    num1 = input('Digite um numero: ')
    operador = input('Escolha o operador: +, -, * ou /: ')
    num2 = input('Digite outro numero: ')

    num1_inteiro = int(num1)
    num2_inteiro = int(num2)
    if operador == '+':
        print(num1_inteiro+ num2_inteiro)
    elif operador == '-':
        print(num1_inteiro - num2_inteiro)
    elif operador == '*':
        print(num1_inteiro*num2_inteiro)
    else:
        print(num1_inteiro/num2_inteiro)
except ValueError:
    print('valor invalido')