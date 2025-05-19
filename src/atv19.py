palavra = 'amanda'
letras_vistas = []

for letra in palavra:
    if letra not in letras_vistas:
        contagem = palavra.count(letra)
        print(f'A letra "{letra}" aparece {contagem} vezes')
        letras_vistas.append(letra)
