
print('Loja super baratão')
total = mais = barato = cont = 0
while True:
    op = ' '
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: '))
    cont += 1
    if cont == 1 or valor < barato:
        barato = valor
        nbarato = produto
    total += valor
    if valor >= 1000:
        mais += 1    
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custou R${barato:.2f}')
