valor = float(input('Qual o valor das compras? R$'))
print('FORMAS DE PAGAMENTO')
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opção = int(input('Qual opção? '))
if opção == 1:
    print('A compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor - (valor * 10 / 100)))
elif opção == 2:
    print('A compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor - (valor * 5 / 100)))
elif opção == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS'.format(valor, valor / 2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas?'))
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, (valor + (valor * 20 / 100)) / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor + (valor * 20 / 100)))
else:
    print('Opção invalida. Tente novamente')


