palavra = input('Digite uma palavra:')
letra_digitada = input('Digite uma letra')
quantidade = 0
for i, letra in enumerate(palavra):
    if letra_digitada in letra:
        quantidade +=1  
        print(f' A letra {letra_digitada} aparece no indice {i}')

print(f'A letra {letra_digitada} aparece {quantidade} vezes ')      
