import matplotlib.pyplot as plt

archivo = open('spotify_data.csv', encoding ='utf-8')

lista = [i.rstrip('\n').split(',') for i in archivo]        # lista removiendo '\n' y separando los elemento de cada linea con ','
canciones = [i[2] for i in lista]                           # Creamos una lista con los nombres de las canciones
duracion = [int(i[5]) for i in lista]                       # Creamos una lista con la duración de cada canción
one_word = [i for i in canciones if ' ' not in i]           # Creamos una lista con las canciones de 1 palabra
duracion_pmd = (sum(duracion)/len(duracion))/60000          # Calculamos el promedio de duración de las canciones
top_10 = ['%.2f' % (float(i)/60000) for i in duracion[:10]]      # Lista con la duración de cada canción (ms a m) formato 0.00m
top_10_mayor = [i for i in top_10 if float(i) >= duracion_pmd]   # Lista con las canciones top 10 con mayor duración al promedio

porcentaje_canciones = (len(one_word)*100)/len(canciones)   # Calculamos el % de canciones con 1 palabra como titulo
mayor_duracion = (len(top_10_mayor)*100)/10                 # % de canciones 1 palabra con mayor duración al promedio
menor_duracion = ((10 - len(top_10_mayor))*100)/10          # % de canciones 1 palabra con menor duración al promedio

print('La relación del top 10 respecto a la duración promedio de cada canción en el top 50 es de:'
      f'\nun {mayor_duracion}% siendo de mayor o igual duración y de un {menor_duracion}% siendo de menor duración.\n')
print(f'El porcentaje de canciones que solo tienen 1 palabra como titulo es del {porcentaje_canciones}%')
print(f'El promedio de duración de cada cancíon es de {"%.2f" %duracion_pmd} minutos')

colors = ['#1271c3', '#4e80a3']                             
labels = ['Una palabra','Más de una palabra']               
plt.pie([len(one_word),len(canciones)],                     # Grafico de torta          
        labels = labels,
        colors = colors,
        autopct = '%.1f %%',
        explode = (0.03, 0))
plt.title('Canciones que solo tienen 1 palabra como titulo') 
plt.show()
