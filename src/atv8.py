print('Escolha uma senha.')
print(f'Mínimo 8 caracteres \n Contém número (in "0123456789") \n Contém letra maiúscula \n Contém símbolo (!@#$%& etc)')
senha = input('Digite a senha: ')


if (len(senha)>=8 and
    any(number.isdigit() for number in senha) and
    any(maiscula.isupper() for maiscula in senha) and
    any(minuscula.islower() for minuscula in senha) and
    any(simbolo in '!@#$%*' for simbolo in senha)):
        print('senha salva com sucesso')
else:
    print('invalido')
  
