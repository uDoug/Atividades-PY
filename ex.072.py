numeros = ('Zero', 'Um', ' Dois' , 'Três', 'Quatro',
 'Cinco', 'Seis', 'Sete', 'Oito',
  'Nove', 'Dez', 'Onze', 'Doze',
   'Treze', 'Quatoze', 'Quinze', 
   'Dezesseis', 'Dezessete', 'Dezoito',
    'Dezenove', 'Vinte')


while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break 
        print('Tente novamente. ', end= '')
    print(f'Você Digitou o número {numeros[n]}')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
print('Fim do programa')
    
 
