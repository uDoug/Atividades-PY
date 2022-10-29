print('='*30)
print('       10 TERMOS DE PA')
print('='*30)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=(' '))
print('Acabou')
