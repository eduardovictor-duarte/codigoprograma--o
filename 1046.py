inicio, fim = map(int,input().split())

if inicio >= fim:
    print(f'o jogo durou {(24 - inicio + fim)} hora (s)')
else:
    print(f'o jogo durou {( fim - inicio)}')