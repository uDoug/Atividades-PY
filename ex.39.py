from datetime import date
ano = int(input('Em que ano você nasceu?'))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 18:
    print('Você já deveria ter se alistado a {} anos.'. format(idade - 18))
    print('Seu Alistamento foi em {}.'.format(ano + 18))
elif idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
    print('Seu alienate será em {}.'. format(ano + 18))
else:
    print('Você tem q se alistar IMEDIATAMENTE!')
