num = int(input('Digite um número para vê seu fatorial: '))
c = 0
fat = 1
for c in range (num, 0, -1):
    fat = fat * c    
print('{}! é igual a {}'.format(num, fat))
