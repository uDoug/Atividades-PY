from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar..')
print('-=-' * 20)
n = int(input('Em que numero eu pensei? '))
n1 = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if n == n1:
    print('PARABÉNS, você venceu')
else:
    print('Pensei no número {}, você perdeu'.format(n1))

