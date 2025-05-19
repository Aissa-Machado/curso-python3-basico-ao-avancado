print('JOGO DA PALAVRA SECRETA')
palavra_secreta = 'pedro'
letra_descoberta = ''

while True:
    letra = input('Digite uma letra: ').strip().lower()
    for secreto in palavra_secreta:
        lista_secreto = list(secreto)
        if letra in lista_secreto:
            letra_descoberta = letra
            print(letra_descoberta)
        if letra not in lista_secreto:
            print('Errou!')

            
 
  