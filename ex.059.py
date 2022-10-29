from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('Qual sua opção? '))
    if opção == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('O produto de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {}, {} é o maior'.format(n1, n2, n1))
        else:
            print('Entre {} e {}, {} é o maior'.format(n1, n2, n2))
    elif opção == 4:
        n1 = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
    else:
        print('Opção invalida')
print('Finalizando programa....')
sleep(3)
print('Fim do Programa')



