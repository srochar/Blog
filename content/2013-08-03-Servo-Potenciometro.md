layout: post.html
title: Jugando con un Servo y Potenci&oacute;metro en Arduino
tags: arduino, potenciometro, Serial, Serial, servo

En este post vamos a controlar un mini-servo a través de un potenciómetro con una ayudita de nuestra placa arduino.

¿Qué necesitamos?:

* 1 protobard
* 1 Servo
* 1 Potenciómetro
* Cables
* 1 Arduino, mi caso UNO

El potenciómetro es un microcontrolador. Tiene 3 cables, uno es la alimentación que es de 5v, el otro es tierra (GND) y por último el que nos entrega las lecturas, este se conecta a un pin análogo. Y por qué un pin análogo, este dispositivo entrega valores entre 0 y 1023 (son 10 bit, que representan 2^10 - 1 valores) que se pueden captar sólo por los pines análogas.

Nuestro otro dispositivo es el mini-servo, lo mismo que el anterior posee 3 cables, la alimentación (5V), tierra y el tercero nos servirá para moverlo, se conecta al pin 9. Para controlar el servo utilizaremos una librería de arduino llamada **Servo.h** que explicaremos más adelante cómo funciona.

El procedimiento es fácil leeremos los valores que tenga el potenciómetro y se los enviaremos al servo. Pero no es tan fácil llevarlo a código . Vamos a ir por parte, primero controlaremos nuestro potenciómetro.

Realizamos las conexiones básicas: 
![Conexión](http://alumnos.informatica.utem.cl/~srocha/imagenes/PotenciometroServo/cirPot.jpg "Circuito Potenciometro")

¿Qué vamos a hacer?

Simple, obtener los valor del potenciómetro y mostrarlos por puerto Serial.

¿Serial? Sí, es nuestro medio de comunicación, donde la arduino nos muestra la información que nosotros queramos.

Y nuestro código serial el siguiente:

~~~{cpp}
int potePin = A0;
int poteVal = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  poteVal = analogRead(potePin);
  Serial.print("El valor del potenciometro: ");
  Serial.println(poteVal);
  delay(10);
}
~~~

Primeras dos líneas:

~~~{cpp}
int potePin = A0;
int poteVal = 0;
~~~

Creo que son fáciles de leer, en la variable entera potePin le asignamos el pin al que conectamos a la arduino. En poteVal, guardaremos los valores entre 0 y 1023.

Setup()

~~~{cpp}
Seria.begin(9600);
~~~

Le decimos a la arduino que habilite la comunicación serial a través del speed 9600.

Ahora viene el procedimiento loop, como su nombre en inglés lo dice, tiene el objetivo de ir repitiendo todo el bloque de códigos que estén adentro.

~~~{cpp}
poteVal = analogRead(potePin);
Serial.print("El valor del potenciometro: ");
Serial.println(potVal);
delay(10);
~~~

AnalogRead(int), es un función de arduino que nos entregalos valores del pin que le enviemos. En este caso del pin A0. PotVal aginamos el valor que nos entrega analogRead.

Serial.print imprime por serial el string que le enviemos :), o una variable, eso hacen las dos siguientes líneas.

Delay() es una pequeña pausa en milisengundos, muy importante para que el potenciometro no colapse con tanto dato que se le pida.

Ahora que entendemos qué hace el código se lo enviamos a la arduino y habilitamos la comunicación serial. Resultados: 

![Serial](http://alumnos.informatica.utem.cl/~srocha/imagenes/PotenciometroServo/resultadosPote.jpg "Resultados Potenciometro")

Tiene un problema este código, más bien sus resultados. Ponganse a análizar los valores que entrega portVal, si uno no mueve el potenciómetro varian los valores levemente en más o menos 1 sin que nosotros lo toquemos. Esto se llama ruido generado por el circuito. Pero tranquilos lo vamos a solucionar.

Agregaremos un "filtro" un arreglo de 10 elementos y calcularemos su promedio y luego lo mostraremos por serial, así vamos a tener un mejor control con el ruido que se forma. Se mantiene el mismo circuito.

Nuevo código:

~~~{cpp}
int potePin = A0;
int poteVal = 0;
int poteProm = 0;
int i;
int arreglopote[10];
int totalpote = 0;

void setup()
{
  Serial.begin(9600);
  for(i = 0; i < 10; i++)
    arreglopote[i] = 0;
  i = 0 ;
}

void loop()
{
  totalpote -= arreglopote[i];
  arreglopote[i] = analogRead(A0);
  totalpote += arreglopote[i];
  i = i + 1;
  if( i >= 10)
  {
    poteProm = totalpote/10;
    Serial.print("El valor del potenciometro: ");
    Serial.println(poteProm);
    i = 0;
  }
  delay(10);
}
~~~

¿ Se entiende ?. Vamos con la explicación.

~~~{cpp}
int poteProm = 0;
int i;
int arreglopote[10];
int totalpote = 0;
~~~

Aparecieron nuevas variables. _PoteProm_ guarda el promedio de las lecturas. _i_ es el simple iterador. _Arreglopote_ es un arreglo donde se guardaran los 10 valores. TotalPote va sumando los valores para luego calcular el promedio.

~~~{cpp}
for(i = 0; i < 10; i++)
	arreglopote[i] = 0;
i = 0 ;
~~~

El for inicia los valores del arreglo en 0, luego vuelve el iterador a 0.

Loop():

~~~{cpp}
void loop()
{
  totalpote -= arreglopote[i];
  arreglopote[i] = analogRead(A0);
  totalpote += arreglopote[i];
  i = i + 1;
  if( i >= 10)
  {
    poteProm = totalpote/10;
    Serial.print("El valor del potenciometro: ");
    Serial.println(poteProm);
    i = 0;
	delay(10);
  }
}
~~~

En loop es donde realizamos más modificaciones, si tratan de entender un poco el código se daran cuenta que sólo se calcula el promedio de 10 valores. Verifiquen los resultados.

Ojo si aumentamos el largo del arrelgo tendremos valores más centrado y con menor "ruido" que se forma. Tener en cuenta igual que seran más valores que leer y se demorará más. Hasta acá llegamos con nuestro potenciómetro, vamos por el mini-servo :).

Para jugar con el mini-servo vamos a darles algunos ángulos básico, que gire 20º,60º,100º y 150º una y otra vez.

Las conexiones:

![Servo](http://alumnos.informatica.utem.cl/~srocha/imagenes/PotenciometroServo/cirServo.jpg "Circuito Servo")

Para el código nos va ayudar la librería **Servo.h**. Instanciamos nuestro objeto de la librería después damos las acciones que tenga este objeto(iniciar, mover, leer, etc).

~~~{cpp}
#include <Servo.h>

int servoPin = 9;
Servo miServo;

void setup()
{
  miServo.attach(servoPin);
}

void loop()
{
  miServo.write(20);
  delay(500);
  miServo.write(60);
  delay(500);
  miServo.write(100);
  delay(500);
  miServo.write(150);
  delay(500);                                          
}
~~~

Si lo compilan y envían a la arudino les debería funcionar y mover el servo como les indique antes.

~~~{cpp}
int servoPin = 9;
Servo miServo;
~~~

La primera asignamos el pin donde conectamos el servo. Luego la parte más importante, creamos un objeto _miServo_ que se puede hacer varias acciones, la primera es decirle a que pin esta conectado.

~~~{cpp}
miServo.attach(servoPin);
~~~

Ahora es como si ya tuviera vida. 

~~~{cpp}
miServo.write(20);
delay(500);
miServo.write(60);
delay(500);
miServo.write(100);
delay(500);
miServo.write(150);
delay(500);
~~~

Útilizamos la acción write, esta mueve el servo al ángulo que se envía. Tiene que ser un valor de 0 a 180, si esta fuera de ese rango lo transforma.

Esto sería para nuestro servo, la librería **Servo.h** nos ayuda mucho y como ven es muy sencillo controlar. Ahora probemos los dispositivos al mismo tiempo :D.

Circuito: 
![Circuito final](http://alumnos.informatica.utem.cl/~srocha/imagenes/PotenciometroServo/cirTotal.jpg "Circuito final")

El código es una mezcla de ambos, optener el valor del potenciómetro y enviarlo al servo, pero recodemos que los valores varían de 0 a 1023 con un simple _map()_. Una función de arduino que cambia un valor en la proporción que indiquemos, o sea 0 sería 0º y 1023 son 180º.

~~~{cpp}
#include <Servo.h>
/*===========Servo===========*/
int servoPin = 9;
Servo miServo;
int angulo=0;
/*===========Potenciometro===*/
int potePin = A0;
int poteVal = 0;
int poteProm = 0;
int i;
int arreglopote[10];
int totalpote = 0;


void setup()
{
  miServo.attach(servoPin);
  Serial.begin(9600);
  for(i = 0; i < 10; i++)
    arreglopote[i] = 0;
  i = 0 ;
}

void loop()
{
  totalpote -= arreglopote[i];
  arreglopote[i] = analogRead(A0);
  totalpote += arreglopote[i];
  i = i + 1;
  if( i >= 10)
  {
    poteProm = totalpote/10;
    Serial.print("El valor del potenciometro: ");
    Serial.println(poteProm);
    angulo = map(poteProm,0,1023,0,180);
    Serial.print("El angulo que se mueve el servo es: ");
    Serial.println(angulo);
    miServo.write(angulo);
    i = 0;
  }
  delay(10);                                         
}
~~~

Y la lectura **Serial** nos muestra:
![Serial](http://alumnos.informatica.utem.cl/~srocha/imagenes/PotenciometroServo/resultadosTotal.jpg "Resultado Final")

Listo el código funciona bien y se mueve sin problemas el servo. Dudas haganlas saber si puedo las respondo. Saludos
