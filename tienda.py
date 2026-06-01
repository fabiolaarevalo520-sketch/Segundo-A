from datetime import datetime

print("****************************")
print("**      BIENVENIDO A      **")
print("* LA TIENDA DE COSMETICOS  *")
print("****************************")
 
num_brochas = 20
num_labiales = 15
num_mascarillas = 10

cosmetico_totales = num_brochas + num_labiales + num_mascarillas

print("por favor ingresa tu nombre")
nombre = input()
print("Por favor ingresa tu apellido")
apellido = input()

#concatenacion
nombre_completo = nombre + " " + apellido
print("Gracias por visitarnos,", nombre_completo)

compras = []

def mostrar_menu():
    print("")
    # print("==============================")
    print("Selecciona la opcion que deseas:")
    print("1: conocer cuantos cosmeticos tiene la tienda")
    print("2: comprar un cosmetico")
    print("3: mostrar comprar")
    print("4: salir del programa")

def mostrar_inventario():
    print("Actualmente contamos con:")
    print("brochas:", num_brochas, "labiales:", num_labiales, "mascarillas:", num_mascarillas)
    print("en total tenemos", num_brochas + num_labiales + num_mascarillas, "cosmeticos")
     
def comprar_cosmeticos():
    carrito = []
    while True:
        print("¿Que cosmetico desea comprar?")
        print("Escribe F para terminar la lista")
        cosmetico = input()

        if cosmetico == "F":
            break

        if cosmetico not in carrito:
            carrito.append(cosmetico)
        else:
            print("ese cosmetico ya se encuentra en el carrito")

    print("El contenido de tu carrito es:")
    for cosmetico in carrito:
        print("  ", cosmetico)

    # Agregar esta compra al historial de compras
    fecha = datetime.now()
    compras.append((nombre, carrito, fecha))

def mostrar_compras():
    print(" ")
    print("***** COMPRAS REALIZADAS *****")

    for compra in compras:
        print(f"    {compra[0]} compro {compra[1]} en {compra[2]}")

while True:
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_cosmeticos()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Saliendo del programa")
        break