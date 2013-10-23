title: Copiar archivos python
tags: python,shutil,os,walk,copiar,ficheros

Por acá al fin, después de una semana agotadora tengo tiempo para escribir un poquito. Les traigo un problema que nos planteó una empresa. 'Copiar todos los ficheros de cierta extensión de una carpeta y sus sub-carpetas a una nueva sin borrar los archivos originales manteniendo el árbol'. Hay varios lenguajes de programación que resuelven el problema.

Un amigo y yo, partimos por la consola de Windows que es lo que quería en ese momento la empresa, pero se volvio complicado, era extrańo, no se entendía el código. Lo mejor era hacer un cambio de enfoque, es por eso que utilizamos python, que es un lenguaje muy fácil de leer y comprender, además su shell interactiva nos ayuda a simplificar ciertas partes del código.

La solución sería; guardar en una lista los archivos de una árbol de carpetas, haciendo un filtro de la extensión, por opción guardaremos tambien la ruta de la carpeta. Luego recorrer la lista de archivos con filtro y por cada archivo, enviar a la nueva carpeta.

Para esto crearé una carpeta con varios archivos de distintas extensiones y a dentro de varias carpetas. Este sera nuestro modelo. 
![Consola](http://alumnos.informatica.utem.cl/~srocha/imagenes/Copiar%20ficheros%20python/modelo.jpg "Consola" )

Ya el primer desafío de obtener una lista de todos los ficheros que tienen las carpetas y sub-carpetas de la librería _os_, podemos ayudarnos con _os.walk(carpeta)_, la que nos devuelve una generador que se puede iterar, en cada iteración entrega una tupla con 3 valores:

* Root: La dirección de la carpeta donde estamos
* Dirs: Lista de todos los directorios por cada iteración
* Files: Lista de todos ficheros que que estan en la carpeta de iteración.

Hagamos una prueba simple:

~~~{python}
import os
carpeta = 'C:/Carpeta'
for root,dirs,files in os.walk(carpeta):
    print 'Carpeta actual:',root.split(carpeta)[1]
    for file in files:
        print file
~~~

Podemos ver que nos muestra los archivos, pero nosotros no queremos sólo el archivo, además necesitamos la dirección completa(_C:/Carpeta/resumen.txt_), acá entra en juego root, que es la dirección completa de la carperta a donde estemos. Entonces con un simple _root + file_ vamos a optener la ruta completa. En _os.path.join_ está la opcion de juntar estos dos string.

Ahora aplicaremos el filtro para ciertas extensiones. Otra vez nos ayudará la librería _os_, tiene una función _splitext_ que retorna una tupla. Esta tupla tiene una particularidad; separa el nombre del archivo, donde el último arreglo contiene la extensión (.txt, .pdf). Para acceder a la última tupla, utilizamos [-1].

Ejemplo:

~~~{python}
import os
extensiones = ['.pdf','.txt','.xlsx']
carpeta = 'C:/Carpeta'
for root,dirs,files in os.walk(carpeta):
    for file in files:
    print 'Carpeta actual:',root.split(carpeta)[1]
        if os.path.splitext(file)[-1] in extensiones
            print os.path.join(root,file)
~~~

En la lista de los archivos que se acepten, guardaremos una mini lista de dos casillas, en la primera almacenaremos la ruta completa del archivo(_os.path.join(root,file)_) y en la segunda el sub-árbol(_root.split(carpeta)[1]_). En python podemos generar lista en una línea, así que todo esto quedaria:

~~~{python}
carpeta = 'C:/Carpeta'
extensiones = ['.pdf','.txt','.xlsx']
lista_archivos =  [ [os.path.join(root,file),root.split(carpeta)[1]] for root,dirs,files in os.walk(carpeta) for file in files if os.path.splitext(file)[-1] in extensiones ]
print lista_archivos 
~~~

Y en _lista_archivo_ tendremos almacenado todos los pdf, txt y xlsx que esten en la carpeta "C:/Carpeta".

Bien, ahora sólo nos queda enviar a la nueva carpeta de destino, para no tener colisiones (si corremos dos veces el programa a la vez) crearemos una carpeta con el nombre de la hora que se arranco el programa.

Con _shutil_ una librería de python copiaremos los archivos de la lista a la nueva carpeta.

Código:

~~~{python}
from datetime import datetime
import os
import shutil
carpeta = 'C:/Carpeta'
destino = 'C:/Datos'

if not os.path.isdir(destino): #nos aseguramos que exista la carpeta
    os.mkdir(destino)
extensiones = ['.pdf','.txt','.xlsx']

lista_archivos =  [ [os.path.join(root,file),root.split(carpeta)[1]] for root,dirs,files in os.walk(carpeta) for file in files if os.path.splitext(file)[-1] in extensiones ]

now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') #genera un string con los datos de Anio-mes-dia-Hora-Minuto-Segundo
carpeta_destino = os.path.join(destino,now)
os.mkdir(carpeta_destino)

for archivo in lista_archivos:
    carpeta_fichero = carpeta_destino + archivo[1]
    if not os.path.isdir(carpeta_fichero): #si no se a existe la carpeta la creamos
        os.mkdir(carpeta_fichero)
    shutil.copy(archivo[0], carpeta_fichero)
~~~

Resultado:
![Resultado](http://alumnos.informatica.utem.cl/~srocha/imagenes/Copiar%20ficheros%20python/resultado.jpg "Resultado")

Si somos curiosos podríamos saber cuántos archivos con extensión pdf hay almacenados en el disco c:, d: y otros. O incluso copiar todos los archivos .jpg por ejemplo del disco c y luego borrarlos :P. Se los planteo. Saludos.
