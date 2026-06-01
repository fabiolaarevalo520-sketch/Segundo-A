#Ciclo, interacion, bucle

#while

i = 0
while i < 10: 
    if i < 5:
        print("El número ", i, "es menor a 5")
    else:
        print("El número", i, "es mayor o igual a 5")
    i += 1

print("Termino la iteracion")

for x in range (1, 11):
    print (x)

while True:
    print("Escribe la opcion deseada")
    print("1: Saludar")
    print("2: Salir")
    respuesta= int(input())

    if respuesta == 1:
        print("Saludes terricola!")
    elif respuesta == 2:
        break

print("Terminando programa")

 


