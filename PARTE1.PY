#1.Programa que permita sumar 2 números
print (75+58+1256) 

#2.Programa que permita multiplicar 3 números
print(854*692*5) 


#3.Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde que X = V*T
v=int(input("ingresa velocidad")) 
t=int(input("ingresa el tiempo"))
print("La distancia reccorrida es: ", v*t,"km/h")


#4. Programa que permita calcular la edad de una persona conociendo el año actual y su año de
nacimiento 
print("ingresa tu año de nacimiento") 
a=int(input())
b=2024
c=b-a
print("edad: ",c)


#5. Programa para calcular el 20% de cualquier número de entrada 
print("Descuento de 20% en todos los jeans") 
j=int(input("Ingresa el precio original del jean: "))
d= j*20/100
p=j-d
print("El precio final es: $",p)


#6. Programa que permita calcular el 30%, el 60% y el 90% de un número cualquiera 
print("Ingrese un número") 
d=int(input())
a=30*d/100
b=60*d/100
c=90*d/100
print("El 30% de",d, "es: ",a)
print(   "El 60% es: ",b)
print(    "El 90% es: ", c)


#7. Programa para calcular el área de un cuadrado. 
print("¿Cuanto mide el primer lado?") 
a=int(input())
print("¿Cuánto mide el segundo lado?")
b=int(input())
print("El área de este cuadrado es: ",a*b,"cm²")  


#8. Programa que permita ingresar 5 números y calcular el promedio

print("                 CALCULAR PROMEDIO\n", "Ingresa 5 valores:\n") 

a=float(input("1."))
b=float(input("2."))
c=float(input("3."))
d=float(input("4."))
e=float(input("5."))
print("El promedio de estos es: ",(a+b+c+d+e)/5)

#9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.   

print("LADRILLO REFERENCIA #246FG89")
print("Precio c/u: $20.000")
print("Ingrese unidades a cancelar")
cantidad=int(input())
unidad_ladrillo=20000
subtotal=int(unidad_ladrillo*cantidad)
total=int(subtotal*1.16)
print("Subtotal: $", subtotal)
print("              +        ")
print("            IVA 16%    ")
print("Total: $", total)

#10. Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

print(" Salario diario: ")
salario_diario=int(input())
print("Dias trabajados: ")
dias_trabajados=int(input())

salario_bruto=int(dias_trabajados*salario_diario)
salario_mensual=(salario_bruto*0.75)

pension=float(salario_mensual*0.1)
Salud=float(salario_mensual*0.15)
print("Salario bruto: $",salario_bruto)
print("Destinado a pension(10%): ",  pension)
print("Destinado a salud(15%):   ", Salud)
print("Salario mensual: $", salario_mensual)



