layout: post.html
title: Sensor Proximidad
tags: proximidad, sensor, arduinio, serial

Tengo en mis manos un sensor de proximidad que utiliza un infrarrojo; [GP2Y0A21](http://alumnos.informatica.utem.cl/~srocha/Download/Sensor%20de%20Proximidad/GP2Y0A21YK.pdf "Manual PDF"). Buscando en internet para saber cómo hacerlo funcionar con arduino no encontré mucha información, debido a esto les explicaré cómo hacer para sacar provecho de este dispositivo.

![Sensor](imagenes/Sensor%20de%20Proximidad/GP2Y0A21.jpg "Sensor GP2Y0A21")

Es fácil entender el cómo funciona y se calcula la distancia. Se envía una señal que al dar con el objeto rebota y llega devuelta al dispositivo. Dependiendo del valor que llega y calculando por un gráfico se puede saber la distancia. Lo que se recibe es "tensión" que puede variar dependiendo del color del objeto que la cantidad de luz que este cerca.

Cable rojo voltaje 5v, amarillo conectado a un análogo y negro a tierra. 

![Conexión sensor proximidad](imagenes/Sensor%20de%20Proximidad/conexion.png "Conexión")

Acá les presento el gráfico tensión vs distancia. 

![Grafico](imagenes/Sensor%20de%20Proximidad/Grafico.png "Grafico")

Deben tener ojo si observan entre 0 - 10 cm se pueden obtener dos tensiones. Si no entiende pueden ver el valor de 1V tiene dos valores 3 cm y 26 cm (aproximadamente). Para evitar estos problemas eviten que la distancia al objeto sea menor a 10 cm.

Habrá que hacer una estimación de esa función yo la hice en excel. Pero obviamente existen más.

Vean el excel para que se vean como logre dar con la función. [Download excel](Download/Sensor%20de%20Proximidad/Estimador.xls)

![Funcion estimada](imagenes/Sensor%20de%20Proximidad/Grafico%20Estimado.png "Funcion Generada por excel")

Habría que calcular la función inversa para que nosotros al darle un valor en tensión nos de vuelva el valor en cm. [Inversa](http://www.wolframalpha.com/input/?i=inverse+y+%3D+14.8*x^%28-0.82%29 "Wolframalpha")

Ok ya se entiende cómo funciona y sabemos cómo calcular la distancia. Llevemos esto a programación y arduino :).

Así debiera funcionar: el dispositivo recibe una señal (que será de 0 a 1023) vía pin análogo, con una simple función (que ya obtuvimos) medimos la distancia.

Pero hay un problema; el valor que nos entrega el pin análogo es un valor entre 0 a 1023, para "transformar" el valor de bit a tensión se aplica una simple regla de tres. 0 -> 0 y 1023 -> 5

Una función simple en arduino sería:

~~~{cpp}
float anal_to_tens(int ana_value)
{
    return (ana_value*5.0)/1023;
}
~~~

Falta sólo la función que devuelva el valor en cm.

~~~{cpp}
float ir_toCm(int pinIR)
{
  float tension;
  int pinValue;
  float valueCm;
  pinValue = analogRead(pinIR);
  tension = anal_to_tens(pinValue);
  
  valueCm = 26.7392/pow(tension,1.21951219512);
  return valueCm;
}
~~~

Y esto sería todo, prueben, acá les dejo el código completo:

~~~{cpp}
float distancia;

float anal_to_tens(int ana_value)
{
  return (ana_value*5.0)/1023;
}

float ir_toCm(int pinIR)
{
  float tension;
  int pinValue;
  float valueCm;
  pinValue = analogRead(pinIR);
  tension = anal_to_tens(pinValue);
  
  valueCm = 26.7392/pow(tension,1.21951219512);
  return valueCm;
}

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  distancia = ir_toCm(A0);
  Serial.print("Distancia : ");
  Serial.print(distancia);
  Serial.println(" Cm");
  delay(10);
}
~~~
