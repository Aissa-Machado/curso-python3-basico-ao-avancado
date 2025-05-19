while True:
    try:
        num1 = int(input('Digite um número: '))
        operador = input('Digite um operador (+, -, *, /): ').strip()
        num2 = int(input('Digite outro número: '))

        if operador not in ['+', '-', '*', '/']:
            print('❌ Operador inválido.')
            continue

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2

        print(f'{num1} {operador} {num2} = {resultado}')

    except ZeroDivisionError:
        print('❌ Erro: Não é possível dividir por zero.')
    except ValueError:
        print('❌ Erro: Digite apenas números inteiros.')

    sair = input('Quer sair? [s] sim: ').strip().lower()
    if sair.startswith('s'):
        break
