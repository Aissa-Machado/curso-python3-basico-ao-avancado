velocidade = 61
local_carro =100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
multado = velocidade > RADAR_1 and local_carro == 99 or local_carro ==101
if multado:
    print('Multado')
else:
    print('Sem multas')