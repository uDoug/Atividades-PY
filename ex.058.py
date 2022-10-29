from random import randint
cont = 1
pc = randint(0, 10)
print('Pensei em um número entre 1 e 10 \nConsegue advinhar?')
player = int(input('Qual seu palpite? '))
while player != pc:
    if player < pc:
        print('Mais.. Tente novamente')
        player = int(input('Qual seu palpite? '))
    else:
        print('Menos.. Tente novamente')
        player = int(input('Qual se palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns!'. format(cont))
