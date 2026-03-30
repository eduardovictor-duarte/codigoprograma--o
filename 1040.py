N1, N2 ,N3, N4 = map(float,input().split(' '))

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1)/ (2 + 3 +4 + 1)
print(f' Media: {media: .1f}')

if media >= 7:
    print('aluno aprovado')
elif media >= 5:
    print('aluno em exame')
    
    N5 = float(input())
    print("Nota do exame: {:.1f}",format(N5))
    media = (media + N5) / 2
    
if media >= 5:
    print('aluno aprovado')
else:
    print(' aluno reprovado') 
    
print(f' Media Final: {media:.1f}')    
