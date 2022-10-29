peso = float(input('Qual é seu peso? (KG): '))
altura = float(input('Qual sua altura? (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL')
elif imc < 25:
    print('Você está com PESO IDEAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Cuidado, você está com OBESIDADE MORBIDA')


