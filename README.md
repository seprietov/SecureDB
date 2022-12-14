# Secure database

___

Aplicación de consola donde se actualiza una base de datos relacional, por medio de web scraping, con información sensible de clientes. Esta data se hace disponible a terceros con diferentes niveles de privilegios. El proyecto tiene como principal enfoque la seguridad de la información.


## Descripción de la aplicación.

Esta es una aplicación de consola que permite la consulta de información sobre usuarios, la cual está almacenada en una base de datos que, mediante el web-scraping, se actualiza. Esta aplicación permite el ingreso, validación de credenciales de dos categorías de usuario. Usuarios “admin”, tienen la posibilidad de crear y eliminar usuarios llamados “requesters”. La creación de ambos tipos de usuarios requiere de la asociación de una contraseña. Los usuarios tipo “requesters” son capaces de hacer queries, dependiendo de su nivel de privilegios, a una base datos que tiene información sensible de usuarios.

Los usuarios “requesters” son capaces de correr queries, bajo ciertas restricciones de palabras para preservar la integridad de la información. Estas restricciones se encuentran en dos tablas, llamadas "insiders" y "outsiders", con el fin de modificar el nivel de acceso que tienen los requesters siendo parte o no de la compañía. Las restricciones serán modificadas en dado caso de que se vea necesario por motivos de seguridad o funcionamiento, por el "admin". Para crear un usuario tipo “requester” se pide el nombre completo de una persona natural, responsable del usuario.

La base de datos está compuesta de cinco tablas “users”, “admins”, “requesters”, “insiders” y “outsiders”. Comenzando por la tabla “admins”, solo disponible para personas con acceso a la máquina que da host al servidor de la base de datos. La tabla “users” es modificada mediante la función “update()” que corre automáticamente cuando un admin ingresa a la aplicación. Esta función borra y vuelve a cargar todos los datos desde la API, lo que permite no mantener información que haya sido eliminada, una de las razones podría ser la cláusula de las políticas de privacidad que permiten a los usuarios la eliminación de sus datos personales. La tabla “requesters” es modificada desde el código si algún usuario “admin” agrega o elimina un usuario “requester”. La tabla “insiders” contiene las palabras restringidas para los usuarios con menor nivel de restricción y la tabla “outsiders” contiene las palabras restringidas para los usuarios con el mayor nivel de restricción, la modificación de estas tablas está restringida para "admins". Como valores iniciales ambas tablas tienen como palabra restringida el nombre de las tablas "insider", "admins" y "outsider", por lo que como “requester” no se pueden correr queries que añadan, eliminen o modifiquen datos de estas tablas.

Esta aplicación requiere del uso de software como XAMPP el cual permite dar host a una base de datos relacional que usa el lenguaje SQL, también se apoya en otra aplicación llamada SQLBackupAndFTP, que permite realizar copias de seguridad como mecanismo de protección en caso de la destrucción, secuestro, corrupción de los datos. La periodicidad de las copias de seguridad pueden ser modificada desde la máquina que está dando host a la base de datos. Estas copias de seguridad también tienen un tiempo de vida máximo en el sistema. 


## Instrucciones para la ejecución de la aplicación.

1. Clonar el repositorio [SecureDB](https://github.com/seprietov/SecureDB.git).
1. Descargar la aplicación XAMPP desde el siguiente [link](https://www.apachefriends.org/download.html) e instalar la aplicación.
1. Oprimimos los siguientes botones en orden: Oprimimos “Start” para la fila “Apache”,  oprimimos “Start” para la fila “MySQL” y Oprimimos “Admin” para la fila "MySQL".    <p align="center"><img src="ImagesSDB/ejecucion1.png" width="50%"></p>
  
1. Elegimos la opción para nueva base de datos y damos click en “Importar”.
    <p align="center"><img src="ImagesSDB/ejecucion2.png" width="50%"></p>
  
1. Usando la herramienta de Seleccionar archivo, ubicamos el archivo “users_info.sql”
    <p align="center"><img src="ImagesSDB/ejecucion3.png" width="50%"></p>
  
1. Damos click en la opción de “Importar”
1. Descargamos SQLBackupAndFTP del siguiente [link](https://sqlbackupandftp.com/download) y corremos la herramienta.
    <p align="center"><img src="ImagesSDB/ejecucion4.png" width="50%"></p>
    
1. Nos vincularnos al servidor al que queremos conectarnos
    <p align="center"><img src="ImagesSDB/ejecucion5.png" width="50%"></p>
    
1. Ahora seleccionamos la base de datos que nos interesa proteger de entre las bases de datos disponibles.
    <p align="center"><img src="ImagesSDB/ejecucion6.png" width="50%"></p>
    
1. Elegimos la configuración de eliminación para nuestras copias de respaldo (el mayor tiempo en el que guardaremos la información). Aquí también se configura la ruta donde se van a guardar las copias de seguridad.
    <p align="center"><img src="ImagesSDB/ejecucion7.png" width="50%"></p>
    
1. Finalmente podemos programar la frecuencia con la cual se van a crear las copias de seguridad de nuestras tablas y base de datos.
    <p align="center"><img src="ImagesSDB/ejecucion8.png" width="50%"></p>
    
1. Ubicamos en nuestro ordenador el archivo “SecureDB.py”, abrimos el archivo con algún Entorno de Desarrollo Integrado y corremos la aplicación, un menú como el siguiente aparecerá.
    <p align="center"><img src="ImagesSDB/ejecucion9.png" width="50%"></p>
    
Al completar estos pasos, la aplicación ya estará en ejecución.

## Código fuente.
El código fuente se puede ver desde el la [master branch](https://github.com/seprietov/SecureDB/tree/master) del proyecto.
