
while True:
    
    try:
        num1 = int(input('Digite um numero: '))
        operador = input('Digite um operador: ')
        num2= int(input('Digite outro numero: '))
    
        if operador not in ['+','-','*','/']:
            print('Operador inválido')
            continue

        if operador == '+':
            resultado = num1 + num2
            print(f'{num1}+{num2} = {resultado}')   
        elif operador == '-':
            resultado = num1 - num2
            print(f'{num1}-{num2} = {resultado}')
        elif operador == '*':
            resultado = num1 * num2
            print(f'{num1}*{num2} = {resultado}')
        elif operador == '/':
            resultado = num1 / num2
            print(f'{num1}/{num2} = {resultado}')
        
    except ZeroDivisionError:
        print('Não e possivel dividir por zero')
    except ValueError:
        print('Apenas numero inteiros.')

    sair = input('Quer sair? [s] sim:').lower().strip()
    if sair.startswith('s'):
        break