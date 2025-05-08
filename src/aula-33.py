try:
    print('Digite de 0 a 23')
    horario = input('que hora é agora? ')
    horario_numero = int(horario)
    if 0 <= horario_numero <= 11:
        print('Bom dia')
    elif 12<= horario_numero <=17:
        print('Boa tarde!')
    else: 
        print('Boa noite')
except ValueError:
    print('valor invalido')