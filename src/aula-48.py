lista_a = ['luiz','maria',True,1.2]
lista_b = lista_a.copy()
lista_a[0] = 'qualquer coisa'

print(lista_a)
print(lista_b)

for nomes in lista_b:
    print(nomes)