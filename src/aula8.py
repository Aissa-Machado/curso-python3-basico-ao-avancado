nome = 'Aissa'
idade = 23
sobrenome = 'Machado'
ano_nascimento = 2001
maior_de_idade = idade >= 18
altura_metros = 1.61
print(f'Nome: {nome}')
print('Idade:',idade)
print(f'Sobrenome: {sobrenome}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'É maior de idade? {maior_de_idade}')
print(f'Altura em metros: {altura_metros}')
if maior_de_idade >= True:
    print(f'Seu nome é {nome} {sobrenome} tem {idade} anos de idade, sendo maior de idade com {altura_metros} de altura')
else:
    print(f'Seu nome é {nome} {sobrenome} tem {idade} anos de idade, sendo menor de idade com {altura_metros} de altura')
