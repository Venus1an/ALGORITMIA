#11. Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento.

print(                       "AÑO 2024")

print("Ingrese año de nacimiento: ")
añoncm=int(input())
if añoncm<= 2006:
    print("Este usuario es mayor de edad")
else:
    print("Este usuario es menor de edad")


#12. Programa para determinar si un número cualquiera ingresado por el usuario es o no positivo. 

print("Ingrese un número: ")
num=float(input())
if num>0:
    print("Este número es positivo")
elif num ==0:
    print("Este número es neutro", num)
else:
    print("Este usuario es negativo")


#13. Programa para determinar cuál es mayor entre 2 números cualquiera ingresados por el usuario
num1= float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
if num1 > num2:
    print("El mayor de los dos es: " + str(num1))
elif num1==num2:
    print("Son el mismo valor")
else:
    print ("El mayor de los 2 es: " + str (num2))
else:
    print ("El mayor de los 2 es: " + str (numME))

#14. Programa para saber si un estudiante del Enrique Olaya Herrera requiere refrigerio. Por disposición de la secretaria de Educación requieren refrigerio los estudiantes de grado sexto hacia abajo.

grado = int(input("Que grado esta cursando: "))

if grado <= 6:
    print ("¡Tienes refrigerio!")
else:
    print ("No tienes refrigerio")

#15. Programa para determinar la mitad de un número ingresado por el usuario es mayor o menor de 100.

num = int(input("Ingresa un numero: "))

num_d = num/2

if num_d >= 100:
    print(f"El numero {num_d} es mayor a 100")
else:
    print(f"El numero {num_d} no es mayor de 100")

#16. Programa en el cual se ingresen 2 números y luego realice las siguientes operaciones: a) Si los números son iguales restarlos b) Si los números son diferentes sumarlos. 

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 == num2:
    print(num1-num2)
else: 
    print(num1+num2)

#17. Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia.   

nombre=(input("Ingrese el nombre del estudiante: "))
codigo=(input("Ingrese código del estudiante: "))
materia=(input("Materia: "))
nota1=float(input("Ingrese la primera nota: "));nota2=float(input("Ingrese la segunda nota: "));nota3=float(input("Ingrese la tercera nota: "))
promedio=(nota1+nota2+nota3)/3


if 4.0<=promedio<5.0:
    print(f"El estudiante: {nombre}\nCodigo:{codigo}\nMateria:{materia}\n APRUEBA")
elif promedio<4.0:
    print(f"El estudiante:{nombre}\nCodigo:{codigo}\nMateria:{materia}\n REPRUEBA")
else:
    print("Evaluar nuevamente")

#18. Programa para determinar cuánto pagara una persona por una compra de la cual se sabe la cantidad de artículos y el valor unitario. Se debe tener en cuenta que el almacén hace un 20% de descuento cuando la compra supera $100000. 

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 100000:
    print("El valor total con descuento es de")
    desc = prod_f*0.20
    print(prod_f-desc)
else:
    print("No tiene descuento")

#19. Programa que permita determinar el total a pagar por una compra de la cual se sabe el valor unitario y la cantidad. Se debe tener en cuenta que se realiza un descuento del 15% por compra inferiores a $20000 y del 35% por compras mayores o iguales a $20000.  

cant_prod = int(input("Cuantos productos adquirio: "))
val_un = int(input("Cuanto es el valor unitario: "))    

total = cant_prod*val_un

if total >= 20000:
    desc = total*0.35
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")
elif total < 20000: 
    desc = total*0.15
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")
#20. Programa para determinar si un número cualquiera ingresado por el usuario es par o impar.(Usar operación Modulo).

num1=int(input("Ingresa un número: "))
if num1 % 2 == 0:
     print("El número es par.")
else:
     print("El número es impar.")

#21. Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”.

print("           TEMPERATURA PROMEDIO SEMANAL"         )
lunes=int(input("Ingrese la temperatura del dia lunes: "))
martes=int(input("Ingrese la temperatura del dia martes: "))
miercoles=int(input("Ingrese la temperatura del dia miercoles: "))
jueves=int(input("Ingrese la temperatura del dia jueves: "))
viernes=int(input("Ingrese la temperatura del dia viernes: "))
sabado=int(input("Ingrese la temperatura del dia sabado: "))
domingo=int(input("Ingrese la temperatura del dia domingo: "))
promedio=(lunes+martes+miercoles+jueves+viernes+sabado+domingo)/7
print("La temperatura promedio de esta semana es de: ", promedio,"°")
if promedio>=35:
    print("Que semana tan calurosa!")
elif promedio<=35 and promedio>=15:
    print("Que clima tan delicioso!")
elif promedio<15:
    print("Que semana tan fria!")
else:
    print("ALERTA CLIMAS EXTREMOS")

#22. Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: a) Por compras entre 10000 y 20000 el 10% b) Por compras entre 20001 y 50000 el 30% c) Por compras superiores a 50000 el 50%.

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 10000 and prod_f <= 20000:
    desc = prod_f*0.10
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 10% {total_f}")
elif prod_f >= 20001 and prod_f <= 50000:
    desc = prod_f*0.30
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 30% {total_f}")
elif prod_f > 50000:
    desc = prod_f*0.50
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 50% {total_f}")
else:
    print("No tiene descuento")

# 23. Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: a) La edad debe ser menor o igual a 18 años b) La estatura debe ser mayor a 180 cm c) El peso debe ser menor o igual a 80 kg.

edad = int(input("Cual es su edad: "))
estatura = int(input("Cual es su estatura: "))
peso = int(input("Cuanto pesas: "))  

if edad <= 18 and estatura >= 180 and peso <= 80:
    print("¡Aceptado en el equipo de baloncesto!")
else:
    print("No fuiste aceptado")
