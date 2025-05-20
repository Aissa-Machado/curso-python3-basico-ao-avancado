# fruta = ['amora','pera','goiaba','maça','abacaxi']
# tamanho_fruta = len(fruta)
# nome = 'Amanda miranda souza'
# tamanho_nome = len(nome)
# print(f'Tamanho nome: {tamanho_nome}, tamanho fruta {tamanho_fruta}')

# numeros = list(range(10,21))
# for i in range(0,len(numeros),2):
#     print(numeros[i])

# gerou erro porque tuplas sao imutaveis para conseguir mudar atreves do indice deve criar uma lista
# cores = ('auzl','verde','amarelo')
# cores[0] = 'azul'
# cores[1] = 'preto'
# print(cores)

# try:
#     numero = input('Digite um numero inteiro: ')
#     if numero.isdigit():
#         numero = int(numero)
#         if numero % 2 == 0:
#             print('par')
#         else:
#             print('impar')
            

# except ValueError:
#     ('Digite apenas numero inteiros')

# numero = 5
# i= 0
# while i < numero:
#     i+=1
#     print(i)

# lista_vazia = []
# nomes= ['Ana','Maria','PEDRO','carlos','Aissa']
# lista_vazia.extend(nomes)
# print(lista_vazia)
# lista_vazia.pop()
# print(lista_vazia)

# cidades = ['contagem','bh','riberao das neves','parana']
# cidades.append('pedro')
# cidades.insert(0,'maria')
# print(cidades)

nome = 'aissa de souza'
primeiro_nome = nome.split()[0]
print(primeiro_nome)