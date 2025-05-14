try:
    # Entrada de dados
    consumo_kWh = input("Digite o consumo em kWh (somente números inteiros): ")
    consumo_residencial_ou_comercial = input("Digite 'r' para residencial ou 'c' para comercial: ").lower()

    if consumo_kWh.isdigit() and consumo_residencial_ou_comercial in ['r', 'c']:
        consumo_kWh_int = int(consumo_kWh)
        tarifa_kWh = 1.47

        # Definindo as taxas extras (exemplo: 10% residencial, 15% comercial)
        residencial = 0.10
        comercial = 0.15

        valor_bruto = consumo_kWh_int * tarifa_kWh

        if consumo_residencial_ou_comercial == 'r':
            valor_final = valor_bruto + (valor_bruto * residencial)
        else:
            valor_final = valor_bruto + (valor_bruto * comercial)

        print(f"Valor final da conta: R${valor_final:.2f}")
    else:
        print("Digite apenas números inteiros para consumo e 'r' ou 'c' para o tipo de uso.")

except ValueError:
    print("Valor inválido.")
