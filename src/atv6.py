try:

#solicita entrada usuario valor do produto e percentual de desconto - solicita entrada usuario
    valor_produto =  input('Qual o valor do produto? ')
    percentual_de_desconto = input('Qual percentual de desconto? (somente números)')
#tranforma a entrada usuario em numeros - transforma em numeros
    percentual_de_desconto_numero = int(percentual_de_desconto)
    valor_produto_numero = int(valor_produto)
#Faz o calculo do desconto - calculca desconto real
    calcula_percentual = percentual_de_desconto_numero / 100
    calcula_desconto = valor_produto_numero * calcula_percentual
#Desconto aplicado, valor final devedor - valor com desconto
    valor_devedor = valor_produto_numero - calcula_desconto


    print(f'Desconto aplicado, valor do produto sai por {valor_devedor} ')
    print(f'Desconto de {percentual_de_desconto_numero}% aplicado. Valor Final: R${valor_devedor:.2f}')
except ValueError:
    print('Valor invalido. Digite apenas números')