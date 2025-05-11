user = 'aissa'
senha = 123456

entrada_usuario = input('Digite seu usuário: ')
entrada_senha = input('Digite sua senha: ')
while entrada_usuario != user or entrada_senha != senha:
    print('Negado')
    entrada_usuario = input('Digite seu usuário: ')
    entrada_senha = input('Digite sua senha: ')

 
print('Acesso Permitido')