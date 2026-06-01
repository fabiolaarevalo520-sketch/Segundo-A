print("Bienvenido al conversor de millas a kilometros")

print("Escribe un número en millas:")
millas = input() #string 

print("Tipo de dato de millas", type (millas))
#Convertir su string a número 
millas = float(millas)
print("Tipo de dato de millas", type(millas))

#1 milla = 1.609 kms
kilometros = millas * 1.609 

print("Millas ingresadas:", millas)
print("Kilometros:", kilometros)