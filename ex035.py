print('\033[1;30m-=\033[m' * 20)
print('\033[1;31mANALISE DE SEGUIMENTOS\033[m')
print('\033[1;30m-=\033[m' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os três segmentos \033[32mPODEM\033[m formar um triângulo')
else:
    print('Os segmentos \033[31mNÃO PODEM\033[m formar um triângulo')

