  print (75+58+1256) #EJ1

print(854*692*5) #EJ2

v=int(input("ingresa velocidad")) #EJ3
t=int(input("ingresa el tiempo"))
print("La distancia reccorrida es: ", v*t,"km/h")

print("ingresa tu año de nacimiento") #EJ4
a=int(input())
b=2024
c=b-a
print("edad: ",c)

print("Descuento de 20% en todos los jeans") #EJ5
j=int(input("Ingresa el precio original del jean: "))
d= j*20/100
p=j-d
print("El precio final es: $",p)

print("Ingrese un número") #EJ6
d=int(input())
a=30*d/100
b=60*d/100
c=90*d/100
print("El 30% de",d, "es: ",a)
print(   "El 60% es: ",b)
print(    "El 90% es: ", c)

print("¿Cuanto mide el primer lado?") #EJ7
a=int(input())
print("¿Cuánto mide el segundo lado?")
b=int(input())
print("El área de este cuadrado es: ",a*b,"cm²")  

print("                 CALCULAR PROMEDIO\n", "Ingresa 5 valores:\n") #EJ8

a=(input("1."))
b=(input("2."))
c=(input("3."))
d=(input("4."))
e=(input("5."))
print=inter("El promedio de estos es: ",(a*b*c*d*e/a+b+c+d+e))

#9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.   

cantidad = int(input("Cuantos productos compro: "))
valorunit = float(input("De cuanto es el valor unitario: "))

iva = valorunit*0.16

total = valorunit+iva

print(f"El total es {total}")

#10. Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

sal_dia = 43333

dias_trab = int(input("Cuantos dias trabajo: "))

sal_sindesc = dias_trab*sal_dia

sal_pen = sal_sindesc*0.10

sal_salu = sal_sindesc*0.15

total_sal = sal_sindesc-sal_pen-sal_salu

print(f"El total del salario es de: {total_sal}")



