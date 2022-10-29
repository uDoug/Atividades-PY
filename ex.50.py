soma = 0
cont = 0
for c in range(0, 6):
    numero = int(input('Digite um Número: '))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print('Você digitou {} n soma dos números pares digitados é {}'.format(cont, soma))



