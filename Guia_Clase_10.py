# Escribir un programa que pida por teclado dos palabras, y a continuación, indique si riman o no.
# Si coinciden las tres últimas letras debe indicar que si riman.
# Si coinciden sólo las dos últimas letras debe indicar que riman un poco.
# En caso contrario, debe indicar que no riman.

p1 = input("ingrese la primera palabra  ")
p2 = input("ingrese la segunda palabra  ")

if p1[-4:0] == p2[-4:0]:
    print("las palabras riman")
elif p1[-3:0] == p2[-3:0]:
    print("las palabras solo riman un poco")
else:
    print("las palabras no riman")

# Un mensaje ha llegado al mail con errores, diseñe un programa que sea capaz de
# corregir estos correos defectuosos, donde el sistema ha reemplazado
# erróneamente los espacios por comas y las comas por ‘#’
# Un ejemplo de mensaje erróneo es: “La,cantimplora,se,calentó#tomar,agua,así,no,tiene,gracia”

mensaje = input("ingrese el mensaje:  ")
new_mensaje = mensaje.replace(",", ' ').replace('#', ', ')
print(new_mensaje)

# Realice un programa que lea tantas cadenas de String como el usuario
# indique por teclado, a continuación, para cada cadena separe cada palabra
# por espacio (“ ”) y muestre en pantalla dos mensajes:
# El primero contiene todas las palabras que ocupan una posición impar en el texto.
# El segundo contiene todas las palabras que ocupan una posición par en el texto.

diccionario = {}
total_textos = int(input('cuantas cadenas de string ingresara?  '))
for i in range (1, total_textos+1):
    diccionario['texto{0}'.format(i)] = input('Ingrese el texto:  ')
     
par = []
impar = []
for i in diccionario.values():
    texto = i.split()
    contador = 0
    for palabra in texto:
        contador += 1
        if contador%2 == 0:
            par.append(palabra)
        else:
            impar.append(palabra)

print(f"las palabras par son '{' '.join(par)}'", f"las impar son '{' '.join(impar)}'")

# Cree un programa donde sea posible ingresar una página de diario de vida,
# el programa deberá comprobar que el escrito cumpla con los siguientes estándares mínimos:
# La primera palabra del escrito debe comenzar con mayúscula.  La primera palabra luego de un punto seguido 
# deberá comenzar con mayúscula.

texto = input('Ingrese el texto:  ')
contador = 0
l = []
m = 0
n = 0

if texto[0].isupper:
    print("la primera palabra comienza con mayuscula")
else:
    print("la primera palabra no comienza con mayuscula")  #hola. Adios. hola

for i in texto:
    if i == '.':
        l.append(contador)
        contador += 1
    else:
        contador += 1

for i in l:
    a = (texto[i+2])
    if a!= ' ':
        n += 1
        if a.isupper():
            m += 1

if m == n:
    print('Todas las palabras despues de un punto seguido comienzan con mayuscula')
else:
    print('No todas las palabras despues de un punto seguido comienzan con mayuscula')


# Cree un programa donde se ingrese una cadena de String y entregue el porcentaje de letras 
# vocales que posee, del total de vocales entregue el porcentaje de aparición de cada 
# vocal y muestra cual es la vocal con mayor frecuencia de la cadena.

texto = input('Ingrese el texto: ').casefold()
z = {}
total_de_vocales = 0
for i in 'aeiou':
    z['{}'.format(i)] = texto.count(i)
    
for k, v in z.items():                               #int() para acortar resultado
    print(f'el porcentaje de aparición de {k} es del {int((v*100)/len(texto))}%')
    total_de_vocales += v                                             

print(f'el porcentaje de vocales es del {int((total_de_vocales*100)/len(texto))}%')
print(f'la vocal con mayor porcentaje de aparición es "{max(z, key = z.get)}"')

# Realice un programa que solicite al usuario una cadena String y, a continuación, solicite al
# usuario un recorte de cadena en un intervalo específico 

texto = input('Ingres el texto:  ')
print('Ingrese el intervalo de recorte:')
a = int(input('inicio:  '))-1
b = int(input('final:  '))-1
print(texto[a:b])

# Realizar un programa donde se solicite una cadena al usuario, a continuación, el programa  imprimirá 
# la cadena invertida caracter a caracter y una cadena invertida en grupos de 4 caracteres.

texto = input('Ingrese el texto:  ')
contador = 0
text = ''
texto_salida = ''
for i in texto:
    texto_salida = i + texto_salida

for i in texto_salida.replace(' ', ''):
    if contador == 4:
        text += ' ' 
        contador = 0
    text += i
    contador += 1

print(texto_salida)
print(text)

# Programa que reciba frases y retorne si estas son Panagramas o no.

print('A continuación ingresara las frases. Cuando desee parar de ingresar frases escriba "listo" ')
while True:
    frase = input('Ingrese la frase:  ')
    if frase == 'listo': break
    frase = frase.lower()
    letras = ''.join(set(frase))
    contador = 0

    for i in letras:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            contador += 1
    if contador == 26:
        print('la frase es un pangrama')
    else:
        print('La frase no es un pangrama')
