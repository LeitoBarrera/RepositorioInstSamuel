import random

def lista_llena():
    return [random.randint(10, 30) for _ in range(30)]

def promedio_tempe(temperaturas):
    return round(sum(temperaturas) / len(temperaturas), 2)

def calcularmitad1(temperaturas):
    return round(promedio_tempe(temperaturas[:15]), 2)

def calcularmitad2(temperaturas):
    return round(promedio_tempe(temperaturas[15:]), 2)

def Tercio1(temperaturas):
    return round(promedio_tempe(temperaturas[:10]), 2)

def Tercio2(temperaturas):
    return round(promedio_tempe(temperaturas[10:20]), 2)

def Tercio3(temperaturas):
    return round(promedio_tempe(temperaturas[20:]), 2)

temperaturas = lista_llena()

print("Lista de temperaturas del mes: ", temperaturas)
print("Promedio del mes: ", promedio_tempe(temperaturas))
print("Promedio de la primera mitad del mes: ", calcularmitad1(temperaturas))
print("Promedio de la segunda mitad del mes: ", calcularmitad2(temperaturas))
print("Promedio del primer tercio del mes: ", Tercio1(temperaturas))
print("Promedio del segundo tercio del mes: ", Tercio2(temperaturas))
print("Promedio del tercer tercio del mes: ", Tercio3(temperaturas))
