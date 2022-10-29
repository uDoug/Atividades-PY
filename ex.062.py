print('='*30)
print('       10 TERMOS DE PA')
print('='*30)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
mais = 10
cont = 1
conttermos = mais

while mais != 0:
    while cont <= mais:
        print(termo, end=(' '))
        termo += razao
        cont += 1
    print('PAUSA   ')
    mais = int(input('Quantos termos você quer mostar a mais? '))
    conttermos += mais
    cont = 1
print('Progressão finalizadas com {} termos mostrados'.format(conttermos))
