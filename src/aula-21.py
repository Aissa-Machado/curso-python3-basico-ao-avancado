entrada = input('[E]ntrar [S]air:' ).replace(' ','').lower()
senha_digitada = input('senha: ')
senha_permitida = '123456'
if entrada == 'e' and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')