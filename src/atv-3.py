#entrada usuario peso e altura
peso = input('Digite seu peso: ')
altura = input('Digite sua altura com duas casas decimais: ')
#tranforma em numero
peso_float = float(peso)
altura_float = float(altura)
#calculo IMC
IMC = peso_float / (altura_float ** 2)
print(f'Seu indice de massa corporal é {IMC:.2f}')

if IMC < 18.5:
    print('indica Magreza')
elif 18.5 <= IMC <= 24.9:
    print(' Esta normal')
else:
    print('Esta em sobrepeso')