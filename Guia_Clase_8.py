# Realizar un algoritmo que resuelva el cuadrado de los N primeros números naturales 
# N es ingresado por el usuario.

def suma_numeros():
    lista = []
    print('cuando quiera dejar de agregar numeros escriba "listo" ')
    while True:
        numeros = (input('Ingrese el numero: '))
        if numeros == 'listo':
            break
        lista.append(int(numeros))
    print(sum(lista))

suma_numeros()

# Realice un algoritmo que reciba un número natural y a continuación determine si es primo o no.

numero = int(input('Ingrese un numero: '))
primo = 1
if numero < 2:
    primo = 0

for i in range(2, numero):
    if numero%i == 0:
        primo = 0

if primo == 1:
    print('es primo')
else:
    print('no es primo')

# Diseñe un algoritmo que resuelva la Conjetura de Collatz, las reglas son:
# Si el numero es par, se divide por 2 y si es impar, se multiplica por 3 y se le suma 1.

numero = int(input('Ingrese el numero: '))

while numero != 1:
    if numero%2 == 0:
        numero = numero/2
        print(numero)
        continue
    else:
        numero = (numero*3)+1
    
    print(numero)

# Desarrolle un programa en Python, tal que, permita el ingreso de un acta de notas. Para esto debe considerar:
# El usuario debe ingresar el nombre del curso.  
# El usuario debe ingresar el nombre de sus alumnos junto a su nota.
# Cuando el usuario determine que ya fueron ingresados todos los alumnos, el programa entregará en pantalla 
# toda la información ingresada.

curso = input('Ingrese el curso: ')
print('A continuación ingrese el nombre y nota de los estudiantes. Cuando desee terminar escriba "listo" ')
alumnos = []
notas = []
n = 0

while True:
    a = input('Ingrese el nombre del estudiante: ')
    if a == 'listo':
        break
    b = input('Ingrese su nota: ')
    alumnos.append(a)
    notas.append(float(b))

print(f'las notas de los alumnos en el curso de {curso} son: ')
for i in alumnos:
    print(f'la nota de {i} es: {notas[n]} ')
    n = n+1

# Diseñe un programa en Python, tal que, presente un menú con las siguientes opciones:
# Calcular el factorial de un número.
# Calcular la suma de un conjunto de números ingresados por el usuario.
# Calcular el promedio de un conjunto de números ingresados por el usuario.
# Salir (el menú se debe volver a mostrar al terminar otra acción)

while True:
    opcion = int(input( ' 1. Calcular el factorial de un numero'
                    '\n 2. Calcular la suma de un conjunto de numeros'
                    '\n 3. Calcular el promedio de un conjunto de numeros'
                    '\n 4. Salir'
                    '\n Ingrese una opcion: '))

    if opcion == 1:
        factorial = int(input('Ingrese el numero: '))
        factorial_resultado = 1
        for i in range (1, factorial+1):
            factorial_resultado = factorial_resultado*i
        print(factorial_resultado)

    if opcion == 2:
        suma_numeros()
    
    if opcion == 3:
        lista_promedio = []
        print('cuando quiera dejar de agregar numeros escriba "listo" ')
        while True:
            numeros = (input('Ingrese el numero: '))
            if numeros == 'listo':
                break
            lista_promedio.append(int(numeros))
        print('el promedio es: ',sum(lista_promedio)/len(lista_promedio))
    
    if opcion == 4:
        break

# Programe un algoritmo en Python, tal que sea capaz de resolver el coeficiente binomial de n sobre k

n = int(input('ingrese n: '))
k = int(input('ingrese k: '))
x = n-k

n_factorial = 1
k_factorial = 1
x_factorial = 1

for i in range(1, n+1):
    n_factorial = n_factorial*i

for i in range(1, k+1):
    k_factorial = k_factorial*i

for i in range(1, x+1):
    x_factorial = x_factorial*i

resultado = n_factorial/(k_factorial*x_factorial)
print(resultado)
