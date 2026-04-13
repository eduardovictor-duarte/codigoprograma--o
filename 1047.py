horainicial, minutoinicial, horafinal, minutofinal = map(int, input().split())

if horainicial == horafinal:
    if minutoinicial == minutofinal:
        print(f'o jogo durou 24 hora(s) e 0 minutos')
     elif minutoinicial > minutofinal
        print(f'o jogo durou 23 hora(s) e {60 - ( minutoinicial - minutofinal)} minuto(s)')
    elif minutoinicial < minutofinal :
        print(f'o jogo duru 0 horas w{ minutofinal - minutoinicial} minuto(s)')
elif horainicial > horafinal:
    if minutoinicial == minutofinal:
        print(f' o jogo durou  {24 - horainicial - horafinal}')              
           