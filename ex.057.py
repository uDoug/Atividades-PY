s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção invalida \nInforme seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado'.format(s))
