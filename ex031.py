distância = float(input('Qual a distância da viagem em Km? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(distância))
if distância >= 200:
    preço = distância * 0.45
else:
    preço = distância * 0.50
print('E o preço da sua viagem será R${:.2f}'.format(preço))


'''if distância >= 200:
    print('E o preço da sua viagem será R${:.2f}'.format(distância * 0.45))
else:
    print('E o preço da sua viagem será R${:.2f}'.format(distância * 0.50))'''


