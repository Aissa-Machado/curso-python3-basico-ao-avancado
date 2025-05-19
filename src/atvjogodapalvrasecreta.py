import os
print('jogo da palavra secrete')
palavra_secreta = 'cachoeira'
letra_acertada = ''
tentatuvas = 0

while True:
    letra_digitada = input('Digite um letra: ').strip().lower()
    tentatuvas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    if letra_digitada in palavra_secreta:
        letra_acertada+=letra_digitada
        palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
                palavra_formada+='*'
    print('Palavra formada: ',palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCE GANHOU!  PARABÉNS')
        print('Tentativa',tentatuvas)
        letra_acertada = ''
        tentatuvas = 0
        