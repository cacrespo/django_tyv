# ¿Cómo colaborar?

1. Antes que nada, necesitas tener un fork del repositorio, haciendo click en el botón correspondiente.

2. Clona el fork del repositorio que acabas de crear:

```
git clone git@github.com:<TU-USUARIO>/django_tyv.git`
```

3. Ingresa en la carpeta que `git clone` creó en tu computadora:

```
cd django_tyv/
```

4. Agrega el repositorio original como «upstream»:

```
git remote add upstream https://github.com/cacrespo/django_tyv.git`
```

5. [Crea un entorno virtual y actívalo](faq.md#Paso-a-paso-para-crear-un-entorno-virtual) (es opcional, pero recomendamos hacerlo).

6. Verifica que estás en la rama principal del repositorio y crea una rama nueva con un nombre que sea representativo del cambio sugerido.

```
git checkout -b nuevo-header
```

7. Realiza todos los ajustes.
8. Cuando hayas terminado tu sesión, debes guardar tus cambios y enviarlos a GitHub para luego solicitar el Pull Request.

```
git add header.html
git commit -m 'incluimos tel en header'
git push origin nuevo-header
```

9. Desde el sitio de Github realiza el PR!

---
### A tener en cuenta :point_left:
Es muy importante [mantener actualiza](faq.md#cómo-mantengo-actualizada-mi-copia-del-repositorio) tu copia local!
