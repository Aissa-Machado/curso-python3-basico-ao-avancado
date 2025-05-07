nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    nome_invertido = nome[::-1]
    quantidade_letras = len(nome)

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('seu nome não contem espaço')
    print(f'Seu nome tem {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    
else:
    print('Desculpe, voce deixou campos vazios')
