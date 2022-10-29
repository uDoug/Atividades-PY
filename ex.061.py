print('='*30)
print('       10 TERMOS DE PA')
print('='*30)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
#decimo = termo + (10 - 1) * razao
cont = 1

while cont <= 10:
    print(termo, end=(' '))
    termo += razao
    cont += 1 

'''while termo != decimo + razao:
    print(termo, end=(' '))
    termo += razao'''

'''for c in range(termo, decimo + razao, razao):
    print(c, end=(' '))
print('Acabou')'''
