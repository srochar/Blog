title: Personalizar terminal de linux
category: misc
tags: linux, terminal, consola, guake, shell

Hoy les traigo un post un poco distinto a los anteriores. Les explicaré como modificar la consola de linux, ya que por lo menos la de ubuntu 14.04 es muy aburrida. Bueno la mía es así:

![Guake + zsh](http://alumnos.informatica.utem.cl/~srocha/imagenes/Personalizar-terminal-de-linux/principal.png)

Es una combinación entre [oh my zsh](https://github.com/robbyrussell/oh-my-zsh) + [guake](https://github.com/Guake/guake/), muy agradable de utilizar, para las personas que les gusta usar harto la consola. Se puede ocultar, dejar encima de todo, abrir otra terminal, auto-completar (que ayuda esto!), usar el tab para mover sobre distintas aplicaciones. Es muy completa, por lo menos yo la uso mucho.

Primero les recomiendo que instalen guake:

##Guake

Es una aplicación que utilizar _guake terminal_ que se fija a la pantalla superior y que aparece cuando uno lo desee ^^, como aparece también uno la puede ocultar (y sigue corriendo en segundo plano).

La instalación es muy simple, por lo menos lo que utilizan ubuntu es:

```bash
sudo apt-get install guake
```
Luego que se instale, pueden usar las preferencias para personalizar mejor y dejar a su comodidad, en las propiedades de guake. Para que la consola aparezca usen el tecla predeterminante _F12_.

![Preferencias](http://alumnos.informatica.utem.cl/~srocha/imagenes/Personalizar-terminal-de-linux/Preferencias_de_Guake_004.png)

Luego de tener instalado guake, vamos por la una shell más poderosa (a mí parecer), que la viene por defecto en ubuntu.

##Oh my zsh

_Oh-my-zsh_ es de código libre que contiene una serie de plugins, temas y mucho más para usar una shell agradable.

Pero antes deben tener instalado zsh, su instalación es simple:

```bash
sudo aptitude install zsh
```

Ahora _oh my zsh_ con el siguiente comando, más aydua en el github de [oh my zsh](https://github.com/robbyrussell/oh-my-zsh)

```bash
wget --no-check-certificate http://install.ohmyz.sh -O - | sh
```

Luego queda sólo cambiar la shell principal, en la consola con el siguiente comando:

```bash
 chsh -s /bin/zsh 
```

Después reinician la sección o reinicien el pc y estará todo listo :D.