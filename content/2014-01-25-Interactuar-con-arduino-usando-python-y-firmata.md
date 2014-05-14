title: Interactuar con arduino usando python y firmata
category: misc
tags: 
Hola holas =) volviendo al mundo virtual después de un par(varias las verdad) de semanas de estres, en la U. Pero sigo vivo y les presentaré un post donde con ayuda de python se puede controlar la arduino.

#PyFirmata

Como en otro post que hice no lo realice por el método de monitor serial, sino con una librería de python (oh amadas 
librerías de python que son tantas xD) nos fácilita el manejo de los pines de la arduino, tanto así como enviar 
información como recibir. La librería es pyfirmata. Su instalación es sencilla con pip.

##Instalar pyfirmata

~~~{bash}
pip install pyfirmata
~~~

Si necesitan más ayuda pueden visitar el repositorio de [pyfirmata](https://github.com/tino/pyFirmata). Necesitan 
tener previamente instalado pyserial.


###Escribiendo....