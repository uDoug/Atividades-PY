s = float(input('Qual o salário do funcionário? R$'))
if s <= 1250:
    s1 = s * 15 / 100 + s
else:
    s1 = s * 10 / 100 + s
print('Quem ganhava R${}{:.2f}{} passa a ganhar R${}{:.2f}{}'.format('\033[36m', s, '\033[m', '\033[32m', s1, '\033[m'))



