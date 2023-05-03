# Dadas dos variables numéricas Var1 y Var2, que el usuario debe ingresar, se
# solicita realizar un algoritmo que intercambie los valores de ambas variables
# y muestre cuánto valen finalmente.

Var1 = input('Ingrese el número: ')
Var2 = input('Ingrese el número: ')

a = Var1
b = Var2
Var1 = b
Var2 = a
print('Var1 =', Var1, 'Var2 =', Var2 )

# Realizar un algoritmo que solicite un número N, y a continuación, lo eleve al
# cuadrado y muestre el resultado en pantalla.

x = float(input('Ingrese un numero: '))
z = x*x 
print(z)

# Realizar un algoritmo donde se ingresen dos notas, una vale 80% y la otra
# vale 20%. Entregue por pantalla la nota ponderada resultante.

n1 = float(input('Ingrese la nota (80%): '))
n2 = float(input('Ingrese la nota (20%): '))
a = n1*0.8 + n2*0.2

print('Su nota ponderada es: ', a)

# Realice un programa que solicite al usuario una cantidad de segundos, y a
# continuación, muestre por pantalla su equivalente en minutos y su
# equivalente en horas.

s = int(input('Ingrese la cantidad de segundos: '))
m = s/60
h = s/3600
print(f'Eso es equivalente a {m} minutos o {h} horas')

# Realice un programa que solicite al usuario una cantidad de segundos y los
# distribuya en: “Cuantas horas, con cuantos minutos y con cuantos segundos”.

segundos = int(input('Ingrese la cantidad de segundos: '))

horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60


print(f'Eso es equivalente a: {horas} horas, {minutos} minutos y {segundos_finales}segundos' )

# Realice un programa que solicite al usuario 3 notas, y a continuación, calcule
# el promedio entre estas y muestre el resultado en pantalla.

n1 = float(input('Ingrese su nota: '))
n2 = float(input('Ingrese su nota: '))
n3 = float(input('Ingrese su nota: '))

x = (n1+n2+n3)/3
print(x)