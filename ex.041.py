from datetime import date

atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade > 25:
    clas = 'MASTER'
elif 25 >= idade > 19:
    clas = 'SÊNIOR'
elif 19 >= idade > 14:
    clas = 'JUNIOR'
elif 14 >= idade > 9:
    clas = 'INFANTIL'
else:
    clas = 'MIRIN'
print('Classificação: {}.'.format(clas))

