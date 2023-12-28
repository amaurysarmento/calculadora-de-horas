print('Voce deve colocar valores entre 0 e 23')

horaInicial = int (input('Digite a hora inicial:\n'))
#minutoInicial = input('Digite o minuto inicial:\n')

horaFinal =  int (input('Digite a hora final:\n'))
#minutoFinal = input('Digite o minuto final:\n')

#exemplo c/ numero: 22h p/ 8h = 10h e 8h p/ 22h = 14h
if horaInicial < horaFinal: 
    #8h p/ 22h = 14h
    result = horaFinal - horaInicial
    print(f'{result}h')


if horaInicial > horaFinal: 
    #22h p/ 8h = 10h
    result = 24 - (horaInicial - horaFinal)
    print(f'{result}h')
