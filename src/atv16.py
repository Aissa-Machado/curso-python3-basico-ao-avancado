palavra = 'amanda'
inverte = palavra[::-1]
print(inverte)
letra_repetida = 0
letra_verificadas = []

for i, letra in enumerate(palavra):
   if letra not in letra_verificadas:
      quantidade = palavra.count(letra)
      if quantidade > 1:
        print(f'A letra {letra} se repete {quantidade} vezes')  
        letra_verificadas.append(letra)