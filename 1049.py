filo = input()
classe = input()
alimentaçao = input()

if filo == 'vertebrado':
    if classe =='ave':
        if alimentaçao == 'carnivoro':
            print('aguia')
        elif alimentaçao =='onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimentaçao == 'onivoro':
            print('homem')
        elif alimentaçao =='herbivoro':
            print('vaca')
elif filo == 'invertebrado':
    if classe == 'inseto': 
        if alimentaçao == 'hematofago':
            print('pulga')
        elif alimentaçao == 'herbivoro':
            print('lagarta')
    elif classe == ' anelidio ':
        if alimentaçao == 'hematofago':
            print(' sanguessuga ')
        elif alimentaçao == 'onivoro':
            print('minhoca')
                       
                    
                    
          
    