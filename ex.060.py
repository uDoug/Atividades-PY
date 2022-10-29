num = int(input('Dgitie um número para caucular seu fatoria: '))
c = num
fat = 1
print('Cauculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end=(''))
    print(' x ' if c > 0 else ' = ', end=(''))
    fat = fat * c
    c -= 1
print('{}'.format(fat))
