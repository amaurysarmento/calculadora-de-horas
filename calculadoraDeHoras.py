import datetime


print('Voce deve colocar valores entre 0 e 23')

horaInicial = int(input('Digite a hora inicial:\n'))
minutoInicial = int(input('Digite o minuto inicial:\n'))

horaFinal = int(input('Digite a hora final:\n'))
minutoFinal = int(input('Digite o minuto final:\n'))

calcRes = datetime.time(horaInicial, minutoInicial)
calcRes1 = datetime.time(horaFinal, minutoFinal)




 
def calcularHora(calcRes, calcRes1):
    ... #ta indicando que vai ser feita alguma coisa nesse bloco de código.

calcularHora(horaInicial,horaFinal) #Aqui to fazendo a funcao receber os valores das hrs pelo argumento.
