title: Montar disco duro automáticamente en linux
category: misc
tags: linux, fstab, montar, 

Muchos de nosotros tiene varias particiones en nuestro disco, por lo menos en mi caso tengo Windows y otra con archivos común entre linux y windows. Las particiones por defecto en linux no se montan de inmediato o en caso de ubuntu cuando la montan, tienen nombre con varios números y letras que es difícil de entender a qué particiones se refiere. Por eso buscando en internet llegue a la solución de montar las particiones automaticamente en linux y dando el nombre que nosotros queramos a las carpetas.

Como son dos particiones debemos crear dos carpetas a las cuales se montarán. Esto es sencillo, hay que crearlas en /media/ con sudo para que no tengamos problemas de privilegio. Como yo tengo dos particiones crearé una de Windodws -para archivos de windows- y Respaldo -para los archivos que tengo en común-. 

	sudo mkdir /media/Respaldo
	sudo mkdir /media/Windows

Teniendo las carpetas debemos indicar a linux que tiene que montarlas ahí. El archivo que debemos modificar es **fstab** que se encuentra en /etc/fstab pero antes de meter mano, debemos saber que tipo de particiones tenemos, por lo que ejecutar en la terminal:

	sudo fdisk -l

En mi caso:
	
    Dispositivo Inicio    Comienzo      Fin      Bloques  Id  Sistema
	/dev/sda1   *        2048    81915434    40956693+   7  HPFS/NTFS/exFAT
	/dev/sda2        81915902   175816703    46950401    5  Extendida
    /dev/sda3       175816704   976773119   400478208    7  HPFS/NTFS/exFAT
    /dev/sda5       167641088   175816703     4087808   82  Linux swap / Solaris
    /dev/sda6        81915904   167641087    42862592   83  Linux

	Las entradas de la tabla de particiones no están en el orden del disco
    
Para sda1 que es windows y sda3 que es el respaldo que tiene archivos en común. Si se dan cuenta ambas son ++ntfs++ este dato es importante tenerlo en cuenta. Ahora vamos a modificar el archivo fstab. Pueden usar cualquier editor de texto en mi caso use nano, pero puede ser gedit también (tiene que ser como super usuario).

	sudo gedit /etc/fstab

Para montar automáticamente sda1 y sda3 es con la siguiente dos líneas que se agregan al final del archivo:

	/dev/sda1   /media/Windows  ntfs    defaults    0   0
	/dev/sda3   /media/Respaldo ntfs    defaults    0   0
    
![Preferencias](http://alumnos.informatica.utem.cl/~srocha/imagenes/Montar-disco-duro-automáticamente-en-linux/fstab.png)

O sea, dispositivo, donde se montara, tipo de partición, opciones (defaults en ambos caso), y 0 0.

Si quieren saber más sobre las opciones pueden leer el siguiente [Link](https://wiki.archlinux.org/index.php/Fstab_%28Espa%C3%B1ol%29)

Sólo falta reiniciar el pc para ver que se hayan montado donde habíamos especificado.