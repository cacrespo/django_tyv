# Preguntas frecuentes
## No puedo resolver un problema. ¿Qué hago?
Preguntar.

## ¿Cómo crear un entorno virtual?
(https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Linux:
* Correr, en la terminal: `python3 -m pip install --user virtualenv`
* Navegar hasta la carpeta donde se desea crear el entorno virtual, y correr `python3 -m venv env`
* Para activar el entorno virtual, en la misma carpeta anterior, correr `source env/bin/activate`
* Para desactivar el entorno virtual, correr `deactivate`

Windows:
* Correr, en la ventana de comandos `py -m pip install --user virtualenv`
* Navegar hasta la carpeta donde se desea crear el entorno virtual, y correr `py -m venv env`
* Para activar el entorno virtual, en la misma carpeta anterior, correr `.\env\Scripts\activate
* Para desactivar el entorno virtual, correr `deactivate`

## ¿Cómo mantengo actualizada mi copia del repositorio?
Es recomendable mantener actualizada nuestra copia local para evitar posibles conflictos entre los archivos que trabajamos y la última versión disponible en el repositorio remoto.

Primero, necesitamos bajar los cambios de __upstream__ (es el nombre que asignamos al repositorio principal).

```
git fetch upstream
```

Luego nos vamos a nuestra rama local, confirmamos e impactamos esos cambios:

```
git checkout main
git merge upstream/main
git push origin main
```

¡Eso es todo!
