palavra = 'pedro'

for i, letra in enumerate(palavra):
    anterior = palavra[i - 1] if i > 0 else 'nenhuma'
    proxima = palavra[i + 1] if i < len(palavra) - 1 else 'nenhuma'

    print(f"A letra '{letra}' está depois de '{anterior}' e antes de '{proxima}'")