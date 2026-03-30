codigo1, quantidade1, Valor1 = map(float,input().split())
codigo2, quantidade2, Valor2 = map(float,input().split())

Custo1 = quantidade1 * Valor1
Custo2 = quantidade2 * Valor2
print(f'Valor a pagar: R${(Custo1 + Custo2):.2f}')


