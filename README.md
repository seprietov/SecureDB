# Secure database

___

Aplicación de consola donde se actualiza una base de datos relacional, por medio de web scraping, información de clientes. Esta información se hace disponible a terceros, con diferentes niveles de privilegios. El proyecto tiene como principal enfoque la seguridad de la información

Como este.
Así puedes usar **negrilla** por si la necesitas.

> #### Por si uieres usar blockcontent
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.


## Descripción de la aplicaión realizada

Esta es una aplicación de consola que permite la consulta de información sobre usuarios la cual está almacenada en una base de datos que, mediante el web-scraping, se actualiza. Esta aplicación permite el ingreso, validación de credenciales de dos categorías de usuario. Usuarios “admin”, tienen la posibilidad de crear y eliminar usuarios llamados “requesters”. La creación de ambos tipos de usuarios requiere de la asociación de una contraseña. Los usuarios tipo “requesters” son capaces de hacer queries a una base datos que tiene información sensible de usuarios.

Los usuarios “requesters” son capaces de correr queries, bajo ciertas restricciones de palabras para preservar la integridad de la información. Estas restricciones se encuentran en dos tablas. llamadas insiders y outsiders esto con el fin de modificar el nivel de acceso que tienen los requesters siendo parte o no de la compañía pudiendo añadir más restricciones a estos. Las restricciones pueden ser modificadas en dado caso de que se vea necesario por motivos de seguridad o funcionamiento. Para crear un usuario tipo “requester” se pide el nombre completo de una persona natural.

La base de datos está compuesta de cinco tablas “users”, “admins”, “requesters”, “insiders” y “outsiders” hay pocas maneras de modificar cada una de las tablas. Comenzando por la tabla “users”, solo disponible para personas con acceso a la máquina que da host al servidor de la base de datos. La tabla “users” es modificada mediante la función “update()” que corre automáticamente cuando un admin ingresa a la aplicación. Esta función borra todos los datos y vuelve a cargar todos los datos desde la API, lo que esto permite es no mantener información que haya sido eliminada, una de las razones podría ser la cláusula de las políticas de privacidad que permiten a los usuarios la eliminación de sus datos personales. La tabla “requesters” es modificada desde el código si algún usuario “admin” agrega o elimina un usuario “requester”, la tabla “insiders” contiene las palabras restringidas para los usuarios con menor nivel de restricción y la tabla “outsiders” contiene las palabras restringidas para los usuarios con la mayor nivel de restricción, la modificación de estas tablas está restringida para admins. Como valores iniciales ambas tablas tienen como palabra restringida el nombre de las tablas insider y outsider, por lo que como “requester” no se pueden correr queries que añadan, eliminen o modifiquen datos de estas tablas.

Esta aplicación requiere del uso de software como XAMPP el cual permite dar host a una base de datos relacional que usa el lenguaje SQL, también se apoya en otra aplicación llamada SQLBackupAndFTP, que permite realizar copias de seguridad como mecanismo de protección en caso de la destrucción, secuestro, corrupción de los datos. La periodicidad de las copias de seguridad pueden ser modificadas desde la máquina que está dando host a la base de datos. Estas copias de seguridad también tienen un tiempo de vida máximo en el sistema. 


## Instrucciones para la ejecución de la aplicación

1. Clonar el repositorio https://github.com/seprietov/SecureDB.git 
1. Descargar la aplicación XAMPP desde https://www.apachefriends.org/download.html e instalar la aplicación.
1. Oprimimos los siguientes botones en orden: Oprimimos “Start” para la fila “Apache”,  oprimimos “Start” para la fila “MySQL” y Oprimimos “Admin” para la fila MySQL.<p align="center"><img src="ejecucion1.jpg" width="50%"></p>
  
1. Elegimos la opción para nueva base de datos y damos click en “Importar”.<p align="center"><img src="ejecucion2.jpg" width="50%"></p>
  
1. Usando la herramienta de Seleccionar archivo, ubicamos el archivo “users_info.sql”
    <p align="center"><img src="ejecucion3.jpg" width="50%"></p>
  
1. Damos click en la opción de “Importar”
1. Descargamos SQLBackupAndFTP del siguiente link https://sqlbackupandftp.com/download y corremos la herramienta.
  <p align="center"><img src="ejecucion4.jpg" width="50%"></p>
1. Nos vincularnos al servidor al que queremos conectarnos
  <p align="center"><img src="ejecucion5.jpg" width="50%"></p>
1. Ahora seleccionamos la base de datos que nos interesa proteger de entre las bases de datos disponibles.
  <p align="center"><img src="ejecucion6.jpg" width="50%"></p>
1. Elegimos la configuración de eliminación para nuestra base de datos (cual es el mayor tiempo en el que guardaremos la información adicional), aquí también vamos a configurar la ruta donde se van a guardar las copias de seguridad.
  <p align="center"><img src="ejecucion7.jpg" width="50%"></p>
1. Finalmente podemos programar la frecuencia con la cual se van a crear las copias de seguridad de nuestras tablas y base de datos.
  <p align="center"><img src="ejecucion8.jpg" width="50%"></p>
1. Ubicamos en nuestro ordenador el archivo “SecureDB.py”, abrimos el archivo con algún Entorno de Desarrollo Integrado y corremos la aplicación, un menú como el siguiente aparecerá
  <p align="center"><img src="ejecucion8.jpg" width="50%"></p>
Al completar estos pasos, la aplicación ya estará en ejecución.


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
