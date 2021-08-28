# ¿Cómo colaborar?

1. Antes que nada, necesitas tener un fork del repositorio, haciendo click en el botón correspondiente.

2. Clona el fork del repositorio que acabas de crear:

`git clone git@github.com:<TU-USUARIO>/django_tyv.git`

3. Ingresa en la carpeta que git clone creó en tu computadora:

`cd django_tyv/`

4. Agrega el repositorio original como «upstream»:

`git remote add upstream https://github.com/cacrespo/django_tyv.git`

5. (es opcional, pero recomendamos hacerlo) Crea un entorno virtual y actívalo:

``python -m venv env
source env/bin/activate   # macOS y Linux
env\Scripts\activate.bat  # Windows``

6. Instala los requerimientos del proyecto:

`pip install -r requirements.txt`
