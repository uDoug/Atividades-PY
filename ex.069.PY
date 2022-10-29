contI = contH = contM = 0
while True:
    sexo = ' '
    op = ' '
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 30)
    
    if idade >= 18:
        contI += 1
    if sexo in 'M':
        contH += 1
    if sexo in 'F' and idade < 20:
        contM += 1
    
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if op in 'N':
        print('-' * 30)
        break
print(f'{contI} pessoas tem mais de 18 anos')
print(f'{contH} Homens foram cadastrados')
print(f'{contM} mulheres tem menos de 20 anos')
