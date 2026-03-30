dias = int(input())

anos = dias//365
dias = dias%365
meses = dias//30
dias = dias%30

print(f'{anos} anos(s)')
print(f'{meses} meses(s)')
print(f'{dias} dias(s)')