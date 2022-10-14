# Secure database

___

Aqui escribimos normal un parrafo como de introducción:) (este es un proyect que bla bla bla para bla bla bla ) los parrafos se separan con saltos de linea.

Como este.
Así puedes usar **negrilla** por si la necesitas.

> #### Por si uieres usar blockcontent
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

1. lista
1. lista

- Vñetas
- Viñetas

## Instrucciones para la ejecución de la aplicación

Así puedes agregar imágenes: 
<p align="center"><img src="descarga.jpg" width="50%"></p>

```Python
#Por si necesitas escrbir código acá
novio = input("Ingrese su nombre:")
if novio == "Sergio":
  print("Vane te ama")
else:
  print(">:v")

```

## Descripción de la aplicaión realizada

Esta es una aplicación de consola que permite la consulta de información sobre usuarios la cual está almacenada en una base de datos que, mediante el web-scraping, se actualiza. Esta aplicación permite el ingreso, validación de credenciales de dos categorías de usuario. Usuarios “admin”, tienen la posibilidad de crear y eliminar usuarios llamados “requesters”. La creación de ambos tipos de usuarios requiere de la asociación de una contraseña. Los usuarios tipo “requesters” son capaces de hacer queries a una base datos que tiene información sensible de usuarios.

Los usuarios “requesters” son capaces de correr queries, bajo ciertas restricciones de palabras para preservar la integridad de la información. Estas restricciones se encuentran en dos tablas. llamadas insiders y outsiders esto con el fin de modificar el nivel de acceso que tienen los requesters siendo parte o no de la compañía pudiendo añadir más restricciones a estos. Las restricciones pueden ser modificadas en dado caso de que se vea necesario por motivos de seguridad o funcionamiento. Para crear un usuario tipo “requester” se pide el nombre completo de una persona natural.

La base de datos está compuesta de cinco tablas “users”, “admins”, “requesters”, “insiders” y “outsiders” hay pocas maneras de modificar cada una de las tablas. Comenzando por la tabla “users”, solo disponible para personas con acceso a la máquina que da host al servidor de la base de datos. La tabla “users” es modificada mediante la función “update()” que corre automáticamente cuando un admin ingresa a la aplicación. Esta función borra todos los datos y vuelve a cargar todos los datos desde la API, lo que esto permite es no mantener información que haya sido eliminada, una de las razones podría ser la cláusula de las políticas de privacidad que permiten a los usuarios la eliminación de sus datos personales. La tabla “requesters” es modificada desde el código si algún usuario “admin” agrega o elimina un usuario “requester”, la tabla “insiders” contiene las palabras restringidas para los usuarios con menor nivel de restricción y la tabla “outsiders” contiene las palabras restringidas para los usuarios con la mayor nivel de restricción, la modificación de estas tablas está restringida para admins. Como valores iniciales ambas tablas tienen como palabra restringida el nombre de las tablas insider y outsider, por lo que como “requester” no se pueden correr queries que añadan, eliminen o modifiquen datos de estas tablas.

Esta aplicación requiere del uso de software como XAMPP el cual permite dar host a una base de datos relacional que usa el lenguaje SQL, también se apoya en otra aplicación llamada SQLBackupAndFTP, que permite realizar copias de seguridad como mecanismo de protección en caso de la destrucción, secuestro, corrupción de los datos. La periodicidad de las copias de seguridad pueden ser modificadas desde la máquina que está dando host a la base de datos. Estas copias de seguridad también tienen un tiempo de vida máximo en el sistema. 

## Instrucciones para la ejecución de la aplicación
