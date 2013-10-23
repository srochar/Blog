layout: post.html
title: Controlar arduino Bluetooth
tags: arduino, android, led, encender, bluetooth

Un tema que siempre he encontrado interesante y entretenido es controlar la arduino a través de android, es por eso que les explicaré cómo logre encender un led y apagarlo controlado por bluetooth desde mi teléfono android. Sólo necesitamos 4 componentes:

* Placa arduino
* Adaptador de bluetooth
* Un led Protobard

Lo primordial es tener un monitor bluetooth, ya que este recibirá y enviará información de la arduino.

Les presento el adaptador de bluetooh que tengo en mis manos: 

![Adaptador](http://alumnos.informatica.utem.cl/~srocha/imagenes/Arduino%20Bluetooth/adaptador.jpg "BT_BOARD V1.3")

Consta de 4 pines como pueden ver en la imagen, funciona así; VCC a 5v (puede ser conectado entre 3.6v - 6v), GND a tierra de la placa, TXD este pin es interesante se conecta al pin RX de la placa arduino(en UNO es el pin 0) y el último es RXD que cómo se imaginan va al TX de la placa arduino.

Tx y Rx será nuestro medio de comunicación de bluetooth a arduino. Tx envía información y Rx recibe, cuando se conectan ambos dispositivos con este protocolo, tendremos un medio de comunicación. 

![Tx y Rx](http://alumnos.informatica.utem.cl/~srocha/imagenes/Arduino%20Bluetooth/conexion.JPG "Ejemplo de comunicación")

Todo lo que salga y entre por serial, sera recibido y/o enviado por tx y rx, así que nos centramos sólo Serial de arudino.

~~~{cpp}
void setup()
{
  Serial.begin(9600);
}
void loop()
{
  Serial.println("Enviado dede la arduino");
  delay(1000);
}
~~~

Y la conexión.

![Conexion Bluetooth](http://alumnos.informatica.utem.cl/~srocha/imagenes/Arduino%20Bluetooth/circuito.jpg "Conexión Bluetooth")

Instalen esta aplicación para ver si recibimos el mensaje [S2 Terminal Blue](https://play.google.com/store/apps/details?id=jp.side2.apps.btterm "Para android") y realicen conexión bluetooth con el módulo. Al conectar nos pedirá una contraseña es '1234' o '0000'.

Si todo anda bien les debería resultar esto en nuestro teléfono. 

![Telefono](http://alumnos.informatica.utem.cl/~srocha/imagenes/Arduino%20Bluetooth/mensaje.png "Mensaje")

Con esto ya hemos avanzado harto, casi un 50%.

Ya podemos contactarnos con nuestra arduino por el teléfono, pero avancemos más allá, encender y apagar el led. Para eso hacemos un programa fácil de arduino que cuando reciba cierto valor (por _Serial_) discrimine y realice una petición, para nuestro ejemplo jugar; con el led. Si no entiendes que es _Serial_ o como recibir datos ve a este [post](http://alumnos.informatica.utem.cl/~srocha/2013/08/10/Serial-arduino/ "Serial Arduino").

El código es simple:

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
    if(Serial.available() > 0)
    {
        info = Serial.read();
        if ( info == '1')
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

En idioma humano sería algo así: "Activa el puerto Serial y el pin 13. Repite esto, recibe un valor por serial según el valor que tiene, toma una decisión; 1 enciende el led, 0 apaga el led, otro valor o desconocido no hacer nada."

Está demás decirles que deben conectar un led al pin 13.

Prueben enviando 0 o 1 con el programa que les di para android (S2 Terminal Blue). Si todo va bien el led conectado al pin 13 debería encender y apagar el led y en nuestro programa de android nos debe mostrar lo siguiente: 

![Resultado](http://alumnos.informatica.utem.cl/~srocha/imagenes/Arduino%20Bluetooth/mensajerecibido.png "Resultado")

Hasta acá este post bastante entretenido, les planteo realizar una aplicación en android que por medio de botones encienda y apaga el led.
