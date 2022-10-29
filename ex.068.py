from random import randint
cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    # ENTRADAS
    op = ' '
    player = int(input('Diga um valor: '))
    while op not in 'PI':
        op = str(input('Par ou Ínpar? [P/I]: ')).upper().strip()[0]
    pc = randint(0, 10)
   # VERIFICA SE É PAR OU ÍMPAR
    if (player + pc) % 2 == 0:
        print(
            f'Você jogou {player} e o computador {pc}. Total de {player + pc} DEU PAR')
    else:
        print(
            f'VOcê jogou {player} e o computador {pc}. Total de {player + pc} DEU ÍMPAR')
   # VERIFICA SE O PLAYER PERDEU
    if op in 'P' and (player + pc) % 2 == 1:
        break
    elif op in 'I' and (player + pc) % 2 == 0:
        break
    else:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1

print('Você PERDEU!')
print(f'GAMER OVER! Você venceu {cont} vezes')
