# El reloj de los 7 segmentos: Tenemos un reloj de 7 segmentos led, cada segundo ciertos segmentos encienden
# mostrando una cantidad determinada de tiempo.
# A las 00:00:00, se encienden 2x2 + 6x6 = 40 leds encendidos.
# ¿Cuántos leds se encienden cuando el reloj marca la hora ingresada por el usuario?.  Formato: 01:30:23.

hora = input('Ingrese la hora (formato:  00:00:00) ')
leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
total_leds = 4
for i in hora:
    if i != ':':
        total_leds += leds[int(i)]

print(total_leds)

# solicite al usuario un número natural y a continuación devuelva su equivalente en base binaria.

numero = int(input('Ingrese un numero: '))
output = ''
while numero != 0:
    if numero%2 == 1:
        numero = (numero-1)/2
        output = '1' + output
    else:
        numero = numero/2
        output = '0' + output
print(output)


# Realice un programa en Python, tal que compruebe si un número natural menor que 1000, ingresado por teclado es:
# Primo, Biprimo, Perfecto o Nariciso.

numero = int(input('Ingrese un numero: '))
# Primo:
primo = 1
if numero < 2:
    primo = 0

for i in range(2, numero):
    if numero%i == 0:
        primo = 0

if primo == 1:
    print('El numero ingresado es primo')

# Narciso:
a = 0
for i in str(numero):
    a += int(i)**len(str(numero))

if numero == a:
    print('El numero ingresado es narciso')

# Perfecto:
numero1 = 0
for i in range(1, numero):
    if numero%i == 0:
        numero1 += i
if numero1 == numero:
    print('El numero ingresado es Perfecto')

# Biprimo

