menor = 0
maior = 0
for c in range(1, 7):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {} Kg'.format(menor))
