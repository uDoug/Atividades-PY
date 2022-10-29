print('BANCO DOUG')
print()
valor = int(input('Quando você quer sacar?'))
valor2 = 0 
cont50 = cont20 = cont10 = cont1 = 0

if valor2 < valor:
    while valor2 < valor:
        valor2 += 50
        cont50 += 1
    if valor2 > valor:
        valor2 -= 50
        cont50 -= 1
    print(f'Total de {cont50} cedulas de R$50')

if valor2 < valor:
    while valor2 < valor:
        valor2 += 20
        cont20 += 1
    if valor2 > valor: 
        valor2 -= 20
        cont20 -= 1
    print(f'Total de {cont20} cedulas de R$20')

if valor2 < valor:   
    while valor2 < valor:
        valor2 += 10
        cont10 += 1
    if valor2 > valor:
        valor2 -= 10
        cont10 -= 1
    print(f'Total de {cont10} cedulas de R$10')

if valor2 < valor:    
    while valor2 < valor:
        valor2 += 1
        cont1 += 1
    if valor2 > valor:
        valor2 -= 1
        cont1 -= 1
    print(f'Total de {cont1} cedulas de R$1')


'''print('BANCO DOUG')
print()
valor = int(input('Quando você quer sacar?'))
total = valor
notas = 0
ced = 50

while True:
    if total >= ced:
        total -= ced
        notas += 1
    else:
        if notas > 0:
            print(f'Total de {notas} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        notas = 0
        if total == 0:
            break              '''