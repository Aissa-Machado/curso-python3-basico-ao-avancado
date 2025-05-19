palavra = 'pedro'
nova_palavra = ''
for i, letra in enumerate(palavra):
    if letra in 'aeiou':
        nova_palavra +='*'
    else:
        nova_palavra+= letra
print(nova_palavra)