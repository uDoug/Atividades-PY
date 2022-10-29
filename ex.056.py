total = 0
velho_idade = 0
cont_m = 0
velho_nome = ''
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    total += idade
    if sexo in'Mm':
        if idade > velho_idade:
            velho_idade = idade
            velho_nome = nome
    elif sexo in 'Ff' and idade < 20:
        cont_m += 1
print('A média de idades é {}'.format(total/4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho_idade, velho_nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_m))
