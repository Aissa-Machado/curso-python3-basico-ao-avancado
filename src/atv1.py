from datetime import datetime

#pergunta ao usuario ano nascimento
ano_nascimento = input('Em que ano voce nasceu? ')

if not ano_nascimento.isdigit():
    print('Voce não digitou o ano de nascimento')
else:
#string passa a ser numero, pega ano atual
    ano_nascimento_numero = int(ano_nascimento)
    ano_atual = datetime.now().year
#calculo ano atual menos ano de nascimento pra desconri idade
    idade = ano_atual - ano_nascimento_numero
#conta quantos dias a pessoa esta viva
    conta_dias = idade * 365
    conta_meses = idade * 12
    print(f'Voce tem {idade} anos de idade, {conta_dias} em dias e {conta_meses} em meses ')