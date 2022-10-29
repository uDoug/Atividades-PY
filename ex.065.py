
n = float(input('Digite um Número: '))
op = 'S'
soma = cont = maior = menor = 0

while op in 'Ss':
    if cont == 0:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    
    if op in 'sS':
        n = float(input('Digite um Número: '))
print('Você digitou {} números e a media foi {}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {:.1f}'.format(maior, menor))
