# Diseñe un algoritmo que lea dos números por teclado, a continuación, el
# programa debe imprimir un mensaje que defina cual es mayor o si son
# iguales.

a = float(input('ingrese un numero: '))
b = float(input('ingrese un numero: '))

if a > b:
    print(f'{a} es mayor que {b}')
elif a < b:
    print(f'{b} es mayor que {a}')
else: 
    print('Ambos numeros son iguales')

# Realizar un algoritmo donde se ingrese el nombre de una asignatura junto a sus tres notas:
# La primera pondera 50%, la segunda pondera 30%, la tercera pondera 20%.
# El programa deberá determinar si el alumno pasó o no la asignatura.

asignatura = input('Ingrese la asignatura: ')
n1 = float(input('Ingrese su primera nota: '))*0.5
n2 = float(input('Ingrese su segunda nota: '))*0.3
n3 = float(input('Ingrese su tercera nota: '))*0.2

if (n1+n2+n3) >= 4:
    print(f'Felicidades aprobaste {asignatura}')
else:
    print(f'Lo siento, no aprobaste {asignatura}')

# Una tienda realiza un descuento del 13% sobre la compra, si son realizadas en los meses de: 
# marzo, abril o mayo. Realice un algoritmo que reciba el precio de una compra, el mes (por número o nombre)
# y si corresponde aplique el descuento indicando por pantalla el precio final de la compra.

compra = int(input('Ingrese el total de la compra: '))
mes = input('Ingrese el mes en que realiza la compra: ')
if mes == 'Marzo' or 'marzo' or 'Abril' or 'abril' or 'Mayo' or 'mayo':
    total_compra = compra - compra*0.13
    print(f'Su nuevo total es: {total_compra} pesos')
else:
    print('No aplica descuento')

# Realizar un algoritmo que, dado un número entero, indique en pantalla si este
# es par o impar, si el número es igual a cero, se debe indicar que es igual a cero

a = int(input('Ingrese el numero: '))

if a == 0:
    print('el numero no es par')
elif a%2 == 0:
    print('el numero es par')
else:
    print('el numero no es par')

# Realizar un algoritmo que, dado un año, este indique si es un año bisiesto o no. 
# Las condiciones son las siguientes: Si es divisible por 4 y no es divisible 100 es bisiesto. 
# Si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto.

year = int(input('Ingrese el año: '))
if year%4 == 0:
    if year !=0: 
        print(f'el año {year} es biciesto')

elif year%100 == 0:
    if year%400 == 0:
        print(f'el año {year} es biciesto')

else: 
    print(f'el año {year} no es biciesto')

# Hacer un algoritmo que lea un número menor que 1000: 
# Si el número tiene un dígito, deberá elevarlo al cuadrado y mostrar su resultado.
# Si el número es de dos dígitos, multiplicarlo por dos y mostrar su resultado.
# Si el número es de tres dígitos, restarle cien y mostrar el resultado.
# En otro caso, mostrar la leyenda “Número no válido”.

numero = int(input('Ingrese un numero menos a 1000: '))

if len(str(numero)) == 1:
    print(numero*numero)
elif len(str(numero)) == 2:
    print(numero*2)
elif len(str(numero)) ==3:
    print(numero-100)
else:
    print('numero no valido')

