try:
    print('Digite apenas números')
    print('Digite notas de 1 a 10.')
    #entrada usuario
    entrada = input('Digite as 3 notas separadas por espaço: ')
    nota1, nota2, nota3 = map(float,entrada.split())
    #calcula Nota Final
    nota_final = (nota1 + nota2 + nota3) / 3
    #verifica media, recuperação, reprovado
    if nota_final >=7:
        print('Aprovado')
    elif 5 <= nota_final <=6:
        print('Recuperação')
    else: 
        print('Reprovado')
except ValueError:
    print('Voce digitou uma nota invalida.')

