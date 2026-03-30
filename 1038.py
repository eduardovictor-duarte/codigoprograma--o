codigo, quantidade = map(float,input().split(' '))

if(codigo ==1):
    precototal = 4.00 * quantidade
elif(codigo == 2):
    precototal = 4.50 * quantidade
elif(codigo == 3):
    precototal = 5.00 * quantidade
elif(codigo == 4):
    precototal = 2.00 * quantidade
elif(codigo == 5):
    precototal = 1.50 * quantidade
    
print(f'total: R${precototal:.2f}')     
                