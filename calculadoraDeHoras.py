import datetime
from datetime import datetime, timedelta

print('Voce deve colocar valores entre 0 e 23')

horaInicial = int (input('Digite a hora inicial:\n'))
minutoInicial = int (input('Digite o minuto inicial:\n'))

horaFinal = int (input('Digite a hora final:\n'))
minutoFinal = int (input('Digite o minuto final:\n'))

calcRes = datetime.time(horaInicial, minutoInicial)
calcRes1 = datetime.time(horaFinal, minutoFinal)

print(calcRes, calcRes1)

res = calcRes - calcRes1

print(res)



# def calcularHora(l1, l2):
#     hrInit = datetime.now(l1)
#     hrFin = datetime.now(l2)
#     res = hrInit - hrFin
#     print(res)

# calcularHora(horaInicial, horaFinal) #Aqui to fazendo a funcao receber os valores das hrs pelo argumento.
