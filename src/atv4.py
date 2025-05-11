num = input('Digite um numero: ')
try:
    num_inteiro = int(num)
    if num_inteiro % 2 == 0:
        print('par')
    else:
        print('impar')
except ValueError:
    print('Valor invalido')
