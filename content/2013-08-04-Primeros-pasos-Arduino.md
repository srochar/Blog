title: Primeros pasos Arduino
tags: arduino, basico, serial, hola mundo, analogo, digital

Primero ¿Qué es una arduino ? . Es una placa programable donde a través de sus pines nos da la facilidad de interactuar con ellos. Básicamente de divide en dos partes, bueno así lo veo yo. La parte de conexiones, ¿ qué pin esta conectado el led, el pin 12 utilizaremos de salida, etc. La otra es decirle a la arduino en sí cómo proceder, enciende el pin 13, leer la entrada del 12, da un pause de 2 segundos, etc.

Existen varios tipos de arudino: 

* Arduino Mega
* Arduino Uno
* Arduino ethernet
* Arduino bluetooth
* ... muchas más

Todas son diferentes entre sí, por ejemplo la Mega una placa muy potente que intrega mucho pines, la UNO es la que yo tengo es más pequeńa y simple, muy básica. Y así van variando.

Los principales pines son; los digitales, análogos, 5v, 3.3v y GND(tierra). Voy a explicar la diferencia entre análogo y digital. Tal vez la forma más simple de explicar su diferencia es imaginando un aparato. Todos o la gran mayoría hemos jugado play station, centremonos en el joystick, para mover a nuestros personajes teníamos dos opciones la parte análoga(círculo de abajo) y la digital(las flechas básica). Sí y sólo cuando precionabamos las flechas el personaje recién se movía, en cambio el análogo podiamos darles velocidad mientras más arriba más rápido iba. Entonces la parte digital toma o no un valor, expresando esto es 0 o 1, bajo o alto. La parte análogo es más completa por así decirlo, en la arduino toma valores de 0 al 1023, que son representando en 10 bits, 2^10 - 1 valores.

Ahora es correcto que existen dos tipos de pines(análogo y digitales), pero también dos forma de útilizarlos. Por ejemplo pensemos en un led y botón, los dos son digitales. El led se apaga o se enciende, botón se presiona o no pero acá radica su diferencia, por así decirlo al led le envíamos energía en cambio en el botón recibímos. Esta es la diferencia, se pueden ocupar los pines como salida de voltaje o entraba.

Los otros 3 pines(5 v, 3.3 v y GND) son para hacer funcionar un dispositivo externo.

Vamos a la parte más entretenida, bueno para mí jajaja, programar la placa. La idea es escribir en un lenguaje que se entienda para nosotros(personas) y arduino. Primero les cuento que se programa en un lenguaje muy parecido a C si tienen conocimientos de este lenguaje les parecera más sencillo, para enviarle la rutina que programemos se hace a traves de un puerto COM. Lo principal para el código fuente son dos procedimeintos(los void ) el _setup()_ y _loop()_. En _setup()_ inciamos todas los pines que vamos a útilizar. En _loop()_ es el código que se irá repitiendo siempre. No explicaré los tipos de datos básicos que son los mismos de C(int, char, boolean, void, float...). Si explicaré las funciones principales o más útilizadas.

Descargen el [sotfware](http://arduino.cc/en/Main/Software "Download") desde la página principal de arduino para que vayan probando todo lo que viene. Creen un nuevo fichero.

La principal estrucutura del código de fuente es:

~~~{cpp}
void setup()
{
}

void loop()
{
}
~~~

Conectamos nuestra placa al pc y cargamos el código fuente. 
![modulo](http://alumnos.informatica.utem.cl/~srocha/imagenes/Primeros%20pasos/cargar.jpg "Software")

Bueno, este programa no tiene nada interesante, realicemos el famoso hola mundo. Debo confesar que es el _Hola Mundo_ más extrańo que he echo jaja.

Necesitamos un led y una placa, yo voy a usar la arduino UNO.

Los led tiene dos patitas y para encenderlo debemos darle energía(+) por uno y el otro enviar a tierra(o negativo -). Si bien tenemos los pin para enviar energía y tierra(pin GND), debemos tener precaución, la salida de un pin digital es de 5v. Un led con este voltaje colpasaría muy rápido. La solución sería aplicar la **ley de ohm** y poner una resistencia antes para que baje el voltaje.

Resistencia = Volataje/Corriente

El voltaje que debe recibir el led es de 1,8 v y tiene que haber una corriente de 15 mA. El pin entrega 5v entonces:

Resistencia = (5v - 1,8 v)/0,015mA = 213,333...

O sea una resistencia de 220 ohm. Pero había dicho que sólo necesitaba un led y la placa. Ajá acá va el truco, la arduino por medio del pin 13 y su pin GND que esta justo al lado tiene una resistencia de 220 ohm, lo que es ideal para encendeer el led, es como si la arduino pensara en nosotros :P.

Entonces nos queda: 
![Led](http://alumnos.informatica.utem.cl/~srocha/imagenes/Primeros%20pasos/cirLed.jpg "Led")
**(Ojo la _patita_ con dobles va al voltaje o la más larga)**

~~~{cpp}
int pinLed = 13;

void setup()
{
  pinMode(pinLed,OUTPUT);
}

void loop()
{
  digitalWrite(pinLed,HIGH);
  delay(1000);
  digitalWrite(pinLed,LOW);
  delay(1000);
}
~~~
 
Ahora aplicaremos un poco de conocimiento que hemos aprendido.

~~~{cpp}
int pinLed = 13;
~~~

Esto llama variable global, el int que tiene antes es de _Integer_ que significa que sera una variable de valores enteros(... -1, 0, 1 ...) lo siguiente es el nombre que le daremos a esta variable tiene que ser bastante representativo, nuestro caso la llamaremos _pinLed_, el valor que viene es la asignacion que le daremos, como el led esta conectado al pin 13, le damos ese valor.

~~~{cpp}
void setup()
{
  pinMode(pinLed,OUTPUT);
}
~~~

La famosa función _setup()_. Como expliqué antes acá se establece el estado de los pines. Usamos una función llamada _pinMode_, que en nuestro lenguaje sería "usa el pin x como salida o entrada", en nuestro caso utiliza el pin _pinLed(13)_ como _OUTPUT_(que en ingles es salida).

~~~{cpp}
void loop()
{
  digitalWrite(pinLed,HIGH);
  delay(1000);
  digitalWrite(pinLed,LOW);
  delay(1000);
}
~~~

_HIGH_ y _LOW_ son constante de arduino que tiene el valor de 1 y 0 respectivamente. _DigitalWrite_ que se interpreta como "en el _pinLed(13)_ se encienda(_HIGH_) o apague(_LOW_)". _Delay()_ es una pause en ms, 1000 ms = 1 segundo, o sea toma una pausa de 1 segundo.

En nuestra palabras todo el programa se leería como: Útiliza el pin 13 como salida de energía. Luego enciende el pin 13, espera 1 sengundo, apaga el pin 13, espera 1 segundo, repite esto sin interrupción.

Hemos terminado, el famoso _Hola Mundo_ de arduino :).

Como pudieron observar entender el lenguaje de arduino es simple, sólo debemos tener precaución de cómo vamos a útilizar los pines y dar bien las instrucciones al código fuente.
