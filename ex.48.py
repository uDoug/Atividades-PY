soma = 0
contnum = 0
for cont in range(1, 501):
    if cont % 3 == 0 and cont % 2 == 1:
       soma = soma + cont
       contnum = contnum+1
print('A soma dos {} números é igual a {}'.format(contnum, soma))
