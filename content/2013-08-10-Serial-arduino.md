title: Serial arduino
tags: Serial,arduino,comunicacion,COM

Si ya probaste el famoso [_hola mundo_](http://alumnos.informatica.utem.cl/~srocha/primeros-pasos-arduino.html "Primeros Pasos Arduino") en arduino (encender y apagar el led) acá les traigo algo un poco más avanzado: controlar cuándo encender el led, a través de la comunicación serial.

![Portada](imagenes/Serial%20Arduino/portada.png "Monitor Serial")

En el momemto que conectamos el cable usb de la arduino al computador, se genera un medio de comunación entre ambos dispositivos. El medio para la arduino se llama _Serial_ y en el computador se escucha el puerto _COM_. Hay distintos puertos _COM(COM1,COM2, etc)_, según el que se haya creado al momento de conectar la arduino. 

Se puede enviar información a la arduino desde el pc o viceversa.

Lo importante es como explotar la interacción, para ello el software de arduino tiene un programa que escucha el puerto _COM_ y también tiene la posibilidad de enviar información por él. Para la versión 1.0.5 del software con _crtl+m_ se abre el programa. 
![COM3](imagenes/Serial%20Arduino/pantallaSerial.jpg "Serial COM")

Es una pequeńa ventana que tiene varias opciones; enviar información, recibir información y cambiar el _speed_(del que hablaré más adelante). Esto sería por parte del software, veamos la arduino:

Decirle a la arduino que habilite el medio de comunicación _Serial_ es muy sencillo, en _setup()_ iniciamos la variable así:

~~~{cpp}
Serial.begin(9600)
~~~

Ojo con la mayúscula al principio es importante. Una vez con eso listo, ya arduino sabe a que puerto escuchar y/o enviar información(_speed =9600_). Para enviar información se utiliza _Serial.print("texto")_, se pueden enviar los valores de las variables también.

Falta sólo escuchar datos, esto se hace con _Serial.read()_ que retorna un char, o sea, sólo carácter. Antes de leer el valor debemos asegurarnos que viene con información. _Serial.available()_ es una función que retorna 0 o un valor mayor a 0. Sí es 0 significa que no hay información, en cambio si es mayor a 0 _Serial.read()_ capturará el carácter.

Listo, ya conocemos como enviar y recibir datos en ambos dispositivos, hagamos una prueba:

~~~{cpp}
char info;
void setup()
{
    Serial.begin(9600);
}
void loop()
{
    Serial.println("Esto lo envia arduino");
    if( Serial.available() )
    {
        info = Serial.read();
        Serial.print("Esto usted envio ");
        Serial.println(info);
    }
    delay(1000);
}
~~~

Cargamos a la arduino y habilitamos la comunicación serial en el software(_crtl+m_). Enviaremos un '1, h, 8 y p' a la arduino y verán que los recibe :).

Mi resultado: 

![Serial resultado](imagenes/Serial%20Arduino/resultado.jpg "Mi resultado")

Pero hagamos algo entretenido; juguemos con un led conectado al pin 13. Si recibe un 1 encienda un led y 0 apaga el led e informe qué hizo con el led. 

~~~{cpp}
int pinLed = 13;
char info;
void setup()
{
    Serial.begin(9600);
    pinMode(pinLed,OUTPUT);
}
void loop()
{
    if(Serial.available() > 0) // si existe llega un dato
    {
        info = Serial.read();
        if ( info == '1') // se compara con un caracter
        {
            digitalWrite(pinLed,HIGH);
            Serial.println("Se encendio el led");
        }
        if( info == '0' )
        {
            digitalWrite(pinLed,LOW);
            Serial.println("Se apaga el led");
        }
    }
    delay(1000);
}
~~~

¿Y para qué sirve esto ?. En realidad para muchas cosas; puede controlar la arduino con python por ejemplo o alguien que le envie información por el medio serial. Si tengo tiempo les muestro como juntar python + arduino.
