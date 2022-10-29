casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos deseja financiar? '))
parcelas = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} por mês'.format(casa, anos, parcelas))
if parcelas > salário * 30 / 100:
    print('Empréstimo \033[31mNEGADO\033[m!!')
else:
    print('Empréstimo \033[32mAPROVADO\033[m!!')






