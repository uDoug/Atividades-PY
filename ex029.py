v = float(input('Qual a velocidade atual do carro em km/h? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((v - 80)*7))
print('Tenha um bom dia! Dirija com segurança!.')


