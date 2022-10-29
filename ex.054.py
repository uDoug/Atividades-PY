from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Ano de nascimento da pessoa {}: '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas atingiram a maior idade'.format(maior))
print('{} não atingiram a maior idade'.format(menor))
  