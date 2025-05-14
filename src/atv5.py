user = 'aissa'
senha = '123456'
print('oi')
entrada_usuario = input('Digite seu usuário: ').replace(" ","")
entrada_senha = input('Digite sua senha: ').replace("","")
while entrada_usuario != user or entrada_senha != senha:
    print('Negado')
    entrada_usuario = input('Digite seu usuário: ')
    entrada_senha = input('Digite sua senha: ')

 

print('Acesso permitido')