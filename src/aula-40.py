


while True:
    print('Calculadora')
    num1 = input('Digite primeiro numero: ')
    operador = input('Digite um operador: *,/,+,-:' )
    num2 = input('Digite segundo numero:' )
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    
        if operador == '*':
            print(f'Resultado: {num1_float * num2_float}')
        elif operador == '/':
            print(f'Resultado: {num1_float / num2_float}')
        elif operador == '+':
            print(f'Resultado: {num1_float + num2_float}')
        elif operador == '-':
            print(f'Resultado: {num1_float - num2_float}')

    except ValueError:
        print('valor invalido')
            
    sair = input('Deseja sair da calculadora? Digite [S] para sim ou [N] para não: ').strip().lower()
    if sair == 's':
        print("Encerrando a calculadora.")
        break
      
        