nome = (input()) #nome do vendedor
salario = float(input()) #salario fixo do vendendor
vendas = float(input()) #n de vendas do vendedor

total = (salario + vendas*0.15) 
print(f'total = R$ {total:.2f}')