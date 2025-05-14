nome = 'Aissa'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)

novo_nome = '*'.join(nome)
print(novo_nome)

novo_nome = nome.replace('a','b')
print(novo_nome)