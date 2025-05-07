entrada = input('voce quer "entrar" [e] ou "sair" [s]: ').replace(' ','').lower()
if entrada == 'e':
    print('você entrou no sistema')
elif entrada == 's':
    print('você saiu do sistema')
else:
    print('valor invalido')