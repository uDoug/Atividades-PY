# Pedra Papel Tesoura
from random import randint
from time import sleep
print('Escolha uma das opções')
print('''1 - PEDRA
2 - PAPEL
3 - TESOURA''')
p1 = int(input('opção: '))
pc = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
if p1 == 1 and pc == 3:
    print('O computador escolheu TESOURA você GANHOU')
elif p1 == 1 and pc == 2:
    print('O computador escolheu PAPEL você PERDEU')
elif p1 == 2 and pc == 1:
    print('O computador escolheu PEDRA você GANHOU')
elif p1 == 2 and pc == 3:
    print('O computador escolheu TESOURA você PERDEU')
elif p1 == 3 and pc == 2:
    print('O computador escolheu PAPEL você GANHOU')
elif p1 == 3 and pc == 1:
    print('O computador escolheu PEDRA você PERDEU')
else:
    print('EMPATOU'.format(pc))
    