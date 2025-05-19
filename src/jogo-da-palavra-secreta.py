print(
'''
      JOGO DA PALAVRA SECRETA 
REGRAS: 
Digite apenas uma LETRA por vez;
Máximo 5 tentativas;
Não pode repetir letras;
''')


while True:
    palavra_secreta = 'cachoeira'
    letra_descoberta = ['']
    for letra in palavra_secreta:
         print(palavra_secreta[letra])