primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f' {primeiro_valor} é maior que {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor} é maior {primeiro_valor}')
elif segundo_valor == primeiro_valor:
    print(f'{primeiro_valor} é {segundo_valor} são iguais')
else:
    print('valor invalido, verifique os valores digitados')