DDD = int(input())

cidades ={

    61: "Brasília",
    71: "Salvador",
    11: "São paulo",
    21: "Rio de Janeiro",
    32: "juiz de fora",
    19: "Campinas" ,
    27: "vitoria",
    31: "Belo Horizonte",
}

if DDD in cidades:
    print(cidades[DDD])
else:
    print('DDD não cadastrado')