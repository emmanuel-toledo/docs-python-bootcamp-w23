# Comandos usables en consola

Consultar ubicaciónn de la ruta actual.
```
pwd
```

Acceder a una ruta o folder.

```
cd <ruta>
cd home
```

Vemos los archivos del directorio actual.
```
la
```

Vemos archivos ocultos (archivos ocultos son aquellos que comienzan con un ```.```).
```
ls -a
```

Si vemos un ```.``` y otro ```..```, significa lo siguiente:
- . = referencia de carpeta actual.
- .. = referencia de la carpeta anterior.

Crear un archivo.

```
# Archivo oculto
touch .env

# Archivo no culto
touch notas.txt
```

Crear una carpeta.

```
mkdir <nombre carpeta>
mkdir ejemplo
```

Copiar un archivo.

```
cp <ruta del archivo> <ruta a donde se quiere copiar>
cp /home/notas.txt /home/ejemplo
```

Mover un archivo.

```
mv <ruta del archivo> <ruta a donde se quiere copiar>
mv /home/notas.txt /home/ejemplo
```

Renombrar un archivo.

```
mv <archivo> <nuevo nombre>
mv notas.txt notas-backup.txt
```

Eliminar un archivo.

```
rm <archivo>
rm notas.txt
```

Editor de archivo en terminal. Para salir presionamos ```Ctrl + X```, luego ```Y```, al final ```enter```.

```
nano <archivo>
nano notas.txt
```
