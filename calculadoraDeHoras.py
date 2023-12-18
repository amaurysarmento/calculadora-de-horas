print('Voce deve colocar valores entre 0 e 23.59')

horaInicial = float(input('Digite a hora inicial:\n'))
#minutoInicial = float(input('Digite o minuto inicial:\n'))

horaFinal = float(input('Digite a hora final:\n'))
#minutoFinal = float(input('Digite o minuto final:\n'))

def calcularHora():
   resultHora = (horaInicial - horaFinal) 
   print(resultHora)

calcularHora()