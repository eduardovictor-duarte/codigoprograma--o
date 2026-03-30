Valor = float(input())

if 100 <Valor:
    print('Fora do intervalo')
elif 75 < Valor:
    print('intervalo (75,100]')
elif 50 < Valor:
    print('intervalo (50,75]')
elif 25 < Valor:
    print('intervalo (25,50]')
elif 0 < Valor:
    print('intervalo [0,25]')
else:
    print('fora do intervalo')