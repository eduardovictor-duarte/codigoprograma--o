lados = input().split()

A, B, C = sorted(map(float, lados), reverse=True)

if A >= (B + C):
    print('nao forma triangulo')
else:
    if (A * A) == (B * B + C * C):
        print('triangulo retangulo')
    elif (A * A) > (B * B + C * C):
        print('triangulo obtusangulo')
    else:
        print('triangulo acutangulo')
        
    lados = [A, B, C,]

if lados.count(A) == 2 or lados.count == 2:
    print('triangulos isoceles')
if lados.count(A) == 3:
    print('triangulo equilatero')    
    
    