try:
    numero = input('Digite um número inteiro: ')
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

except:
    print('Voce deve digitar um numéro inteiro.')
##############3
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
##########################
nome = input('Digite seu nome: ').strip()

if not nome:
    print('Voce nao digitou um nome')
else:
    nome_tamanho = len(nome)

    if 1<= nome_tamanho <= 4:
        print('Seu nome é curto')
    elif 5<= nome_tamanho <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

