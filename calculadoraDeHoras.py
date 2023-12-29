print('Voce deve colocar valores entre 0 e 23')

horaInicial = int (input('Digite a hora inicial:\n'))
minutoInicial = int (input('Digite o minuto inicial:\n'))

horaFinal =  int (input('Digite a hora final:\n'))
minutoFinal = int (input('Digite o minuto final:\n'))



#exemplo c/ numero: 22h p/ 8h = 10h e 8h p/ 22h = 14h
if horaInicial < horaFinal and minutoInicial < minutoFinal: 
    #8h p/ 22h = 14h
    result = horaFinal - horaInicial
    resultMnts = minutoFinal - minutoInicial
    print(f'{result}h{resultMnts}') #Funcionando corretamente com os minutos tambem

if horaInicial < horaFinal and minutoInicial > minutoFinal: 
    #8h p/ 22h = 14h
    result = horaFinal - horaInicial - 1 # -1 porque tava 1h a mais.
    resultMnts = 60 - (minutoInicial - minutoFinal)
    print(f'{result}h{resultMnts}')#Funcionando corretamente com os minutos tambem

if horaInicial > horaFinal and minutoInicial < minutoFinal: 
    #22h p/ 8h = 10h
    result = 24 - (horaInicial - horaFinal)
    resultMnts = minutoFinal - minutoInicial 
    print(f'{result}h{resultMnts}')#Funcionando corretamente com os minutos tambem

#Não concluida essa parte do algoritmo
if horaInicial > horaFinal and minutoInicial > minutoFinal: 
    #22h p/ 8h = 10h
    result = 24 - (horaInicial - horaFinal) - 1# A hora ta saindo certa.
    resultMnts = minutoInicial + minutoFinal # Os minutos tão passando pra mais ou pra menos geralmente em 12h
    print(f'{result}h{resultMnts}')