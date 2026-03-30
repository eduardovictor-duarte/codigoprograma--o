A, B, C, = map(float, input().split())
pi= 3.14159

Triangulo = A * C/2
Circulo = C**2 * pi
trapezio = (A + B) *C/2
quadrado = B**2
retangulo = A * B

print(f' Triangulo:{Triangulo:.3f}')
print(f' circulo:{Circulo:.3f}')
print(f' trapezio:{trapezio:.3f}')
print(f' quadrado:{quadrado:.3f}')
print(f' retangulo:{retangulo:.3f}')