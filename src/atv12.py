print('Calculadora')

while True:
    num1 = input('Digite o primeiro número: ')
    operador = input('Digite um operador (*, /, +, -): ')
    num2 = input('Digite o segundo número: ')

    try:
        num1_float = float(num1)
        num2_float = float(num2)

        if operador == '*':
            resultado = num1_float * num2_float
        elif operador == '/':
            if num2_float == 0:
                print("Erro: divisão por zero!")
                continue
            resultado = num1_float / num2_float
        elif operador == '+':
            resultado = num1_float + num2_float
        elif operador == '-':
            resultado = num1_float - num2_float
        else:
            print("Operador inválido.")
            continue

        print(f'Resultado: {resultado:.2f}')

    except ValueError:
        print("Por favor, digite apenas números válidos.")
        continue

    sair = input('Deseja sair da calculadora? Digite [S] para sim ou [N] para não: ').strip().lower()
    if sair == 's':
        print("Encerrando a calculadora.")
        break
