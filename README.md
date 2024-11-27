<img  align="left" width="150" style="float: left;" src="https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/CEI/LOGOTIPO%20leyenda%20color%20JPG%20p.png">
<img  align="right" width="60" style="float: right;" src="http://www.dit.upm.es/figures/logos/ditupm-big.gif">


<br/><br/>


# Práctica ODM con PYTHON-FLASK y MONGOENGINE

## 1. Objetivo

- Desarrollar las 4 operaciones CRUD (Create, Read, Update and Delete) a través de un ODM
- Practicar con un ODM para realizar queries
- Afianzar las ventajas de usar ODMs en el desarrollo de aplicaciones
- Poner en práctica el uso de SPARQL para integrar fuentes de datos externas en una aplicación real

## 2. Dependencias

Para realizar la práctica el alumno deberá tener instalado en su ordenador:
- Herramienta GIT para gestión de repositorios [Github](https://git-scm.com/downloads)
- Entorno de ejecución de Python 3 [Python](https://www.python.org/downloads/)
- Base de datos MongoDB [MongoDB](https://www.mongodb.com/try/download/community)
- Base de datos [Fuseki](https://jena.apache.org/documentation/fuseki2/)

## 3. Descripción de la práctica

La práctica simula una aplicación que permite añadir valoraciones y comentarios sobre películas basada en el patron MVC (Modelo-Vista-Controlador) utlizando la librería Flask de python.
La práctica tambien usa MongoEngine como ODM para poder almacenar los datos de la aplicación en MongoDB, y accede a una base de datos RDF mediante SPARQL.

La **vista** es una interfaz web basada en HTML y CSS que permite realizar diversas acciones sobre las películas como crear, editar, buscar, filtrar, listar o eliminar. La vista esta incluida ya en el codigo descargado.

El **modelo** es la representación de la información de las películas, usuarios y comentarios. En esta aplicación se van a usar dos modelos: User y Movie. Un ejemplo de como están definidos los modelos en esta práctica es el siguiente (la definición  parcial de los modelos se encuentra en `models.py`):

```
class Movie(db.Document):
    _id = db.ObjectIdField(primary_key=True)
    title = db.StringField(required=True)
    uri = db.StringField(required=True)
    slug = db.StringField(required=True, unique=True)
    release_date = db.DateTimeField()
    genres = db.ListField(db.StringField())
    thumbnail = db.StringField()
    duration = db.IntField()
    director = db.StringField()
    actors = db.ListField(db.EmbeddedDocumentField(Actor))
    ratings = db.FloatField()
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()
```
Por sencillez se ha relacionado el User con las Reviews. Es decir en este modelo las reviews van asociadas a un usario.

El alumno deberá  completar el código necesario para generar los modelos de User y Review, incluyendo el atributo referenciado dentro de el modelos de Review.

El **controlador** ejecuta acciones sobre los modelos. El alumno deberá desarrollar varias funciones del controlador para que las acciones que se realicen a través de la página web funcionen correctamente. Para ello, desarrollara las operaciones correspondientes con MongoEngine implementando las operaciones CRUD sobre los objetos User y Reviews, así como otra serie de queries.

En el siguiente video puede observar cuál sería el funcionamiento normal de la aplicación [link](#)


## 4. Descargar e instalar el código del proyecto

Abra un terminal en su ordenador y siga los siguientes pasos.

Clone el repositoro de GitHub
```
git clone https://github.com/BBDD-ETSIT/ODM_PYTHON_SPARQL_GISD.git
```

Navegue a través de un terminal a la carpeta ODM_PYTHON_SPARQL_GISD.
```
cd ODM_PYTHON_SPARQL_GISD
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] > python3 -m venv venv
[WINDOWS] > py.exe -m venv env
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] > python3 -m pip install --user virtualenv
[WINDOWS] > py.exe -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] > source venv/bin/activate
[WINDOWS] > .\env\Scripts\activate
```

Instalamos las dependencias con pip:

```
pip3 install -r flaskr/requirements.txt
```

Debemos tener arrancado MongoDB. Dependiendo de cómo lo hayamos instalado arrancará solo al iniciar la máquina o tendremos que ir a ejecutar el programa "mongod" a la carpeta bin donde hayamos realizado la instalación.

Podemos arrancar el servidor con el siguiente comando. Hasta que no realize el primer ejercicio sobre la configuración de la URI, el servidor no arrancara.

```
flask --app ./flaskr/run.py  run --debug
```

Abra un navegador y vaya a la url "http://localhost:5000" para ver la aplicación.

Si necesita arrancar la aplicación en un puerto diferente al predeterminado puede usar el siguiente comando (reemplazando el 5002 por el puerto correspondiente):

```
flask --app ./flaskr/run.py  run --debug --port=5002
```

En un terminal distinto a donde se está ejecutando la aplicación, ejecutar los seeders para llenar la base de datos con los datos iniciales:
```
mongoimport -d moviesbdnr -c user --file ./flaskr/seeders/user.json --jsonArray
mongoimport -d moviesbdnr -c movie --file ./flaskr/seeders/movie.json --jsonArray
```

Comprobar que los datos han sido guardados en cada una de las colecciones. Para ello, se debe usar la mongo shell para conectarse a la bbdd y realizar un find en cada una de las colecciones.

> [!NOTE]  
> Si ha modificado algun documento de manera indeseada y se quiere volver a restablecer los valores por defecto, borre la base de datos que ha creado y vuelva a arrancar el servidor con flask.

## 5. Tareas a realizar

La primera tarea es inspeccionar todo el código provisto y entender donde están los modelos, las vistas y los controladores, asi como la semilla o seeders.

### 5.1 Definir el modelo de User y completar el de Movie:

El modelo es el que interactúa con la BBDD, por lo tanto se deben definir los modelos faltantes para poder acceder tanto  a los documentos de User  de la base de datos como a los reviews. Para ello debe completar en el fichero `models.py` las  líneas de código que hagan falta. Un ejemplo del esquema de los documentos de user y movies que están almacenados en la base de datos son los siguientes:

**User**:

```
{
	"_id" : "670d392bd5c2c5162183667f",
	"username" : "admin",
	"name" : "Admin",
	"surname" : "AdminSurname",
	"email" : "admin@example.com",
	"password_hash" : "pbkdf2:sha256:600000$y7FnKSqUAoZBtXgd$3eabb3de2c6e75657501e3d5475d3a16142ae34de03491585d72324aa7d85fd0",
	"created_at" : "2023-09-01T00:00:00Z",
	"updated_at" : "2023-09-01T00:00:00Z"
}
```

**Movie**:

```
{
	"_id" : ObjectId("670e6fe1a5e24a431c1e6805"),
	"uri" : "http://www.wikidata.org/entity/Q190050",
	"title" : "Fight Club",
	"slug" : "fight-club",
	"release_date" : "1999-10-15",
	"duration" : 139,
	"thumbnail" : "https://m.media-amazon.com/images/M/MV5BOTgyOGQ1NDItNGU3Ny00MjU3LTg2YWEtNmEyYjBiMjI1Y2M5XkEyXkFqcGc@._V1_.jpg",
	"director" : "David Fincher",
	"genres" : [
		"Drama"
	],
	"actors" : [
		{
			"name" : "Brad Pitt",
			"date_of_birth" : "1963-12-18",
			"biography" : "Brad Pitt nació el 18 de diciembre de 1963 en Shawnee, Oklahoma, EE. UU. Es un actor y productor conocido por Fight Club (1999), Se7en (1995) y Once Upon a Time in Hollywood (2019)."
		},
		{
			"name" : "Edward Norton",
			"date_of_birth" : "1969-08-18",
			"biography" : "Edward Norton nació el 18 de agosto de 1969 en Boston, Massachusetts, EE. UU. Es un actor conocido por Fight Club (1999), American History X (1998) y The Grand Budapest Hotel (2014)."
		}
	],
	"ratings" : 8.8,
	"reviews" : [
		{
			"user_id" : ObjectId("670d392bd5c2c51621836680"),
			"username" : "user1",
			"rating" : 9,
			"comment" : "Un clásico moderno que cuestiona la realidad."
		},
		{
			"user_id" : ObjectId("670d392bd5c2c51621836682"),
			"username" : "jane",
			"rating" : 8,
			"comment" : "Inquietante y profundo."
		}
	],
	"created_at" : "2023-09-01T00:00:00Z",
	"updated_at" : "2023-09-01T00:00:00Z"
}

```
Nótese que en el modelo de Movie el único campo que no está definido es el de review. Por lo tanto debe crear el subdocumento correspondiente a review y luego añadirlo a el modelo Movie.

### 5.2 Rellenar las funciones de los controladores para user y movie que interactúan con la base de datos usando los modelos.

Se provee un esqueleto con todas los funciones que deberá rellenar. El alumno deberá editar los ficheros `controllers/userController.py` y `controllers/movieController.py`.

En cada una de estas funciones se debe hacer uso del ODM MongoEngine o de SPARQL para realizar operaciones con la base de datos y devolver un resultado de la operación.


Las funciones son las siguientes para `controllers/userController.py`:

### read_users()

**Descripción:** Muestra todos los usuarios de la colección  "User"

**Parametros:** Ninguno

**Returns:** Un array de objetos de user

### read_user()

**Descripción:**  Mustra la información de un usuario específico

**Parametros:** username

**Returns:** Un objeto user

### create_user()

**Descripción:**  Crea un usuario nuevo un la colección "User"

**Parametros:** username, name, surname, email, password_hash

**Returns:** Un objeto user con los datos del usuario creado


### update_user()

**Descripción:**  Actualiza un usuario, debe primero realizar la búqueda de un usuario dado su username y luego actualizarlo

**Restricciones:** No se permite cambiar o modificar el username del usuario

**Parametros:** username, name, surname, email, password_hash, country, city

**Returns:** Un objeto user con los datos del usuario actualizado


### add_favorite_movie_to_user()

**Descripción:**  Añade un marcador de favoritos de una pelicula al usuario, debe primero realizar la búqueda de un usuario dado su username y luego añadir una película como favorita dada su movie_id

**Parametros:** username, movie_id, movie_title, movie_slug

**Returns:** Un objeto user con los datos del usuario actualizado


Para `controllers/movieController.py` tenemos:
### read_movies_by_filter()

**Descripción:**  Muestra todas las peliculas que contengan el texto introducido en los campos title, genero y director.

**Parametros:** title, gener, director

**Restricciones:** Solo se piuede realizar la búsqueda por un parámetro a la vez, se debe validar que los parámetros no esten vacíos es decir `None`

**Returns:** Una lista de objetos movie

():
### create_review()

**Descripción:**  Añade una review a una movie dado un movie_slug y los datos del user

**Parametros:** movie_slug, user_id, username, comment, rating

**Restricciones:** Solo se piuede realizar la búsqueda por un parámetro a la vez, se debe validar que los parámetros no esten vacíos es decir `None`

**Returns:** Un objeto movie con la información de la movie y el comentario añadido

### Consulta SPARQL en `read_movie()`


### read_movie()

**Descripción:**  Muestra la información de una película usando SPARQL

**Parametros:** slug

**Returns:** Un objeto movie

### Consulta SPARQL en `read_movie()`

Las tareas principales en este apartado son:

- Modificar el código de la consulta para que la página de una película incluya al menos 5 campos adicionales obtenidos mediante SPARQL a wikidata
- Generar un nuevo fichero de seed con más películas utilizando una consulta SPARQL a wikidata (`extra_movies.json`)
- Descargar toda la información necesaria para las consultas a un fichero `movies.ttl`

Para que la información recogida con SPARQL se muestre en la página web, deberemos añadir el atributo `extra` al objeto película antes de devolverlo en la función `read_movie`.
Para ello, haremos uso de la función `query` del módulo `sparql` presente en el proyecto flaskr.
Esta función envía la consulta SPARQL que pidamos y devuelve los como una lista de diccionarios, donde cada elemento es una fila, cuyas claves son los nombres de las columnas y el valor es la celda correspondiente en esa fila.

Este es un ejemplo de uso para capturar información sobre el país del que es la película:

```python
movie.extra = query('''
    SELECT (?country as ?Pais)
    WHERE {{
      <{uri}> wdt:P495 ?origin .
      ?origin rdfs:label ?country .
      FILTER(lang(?country) = "es")
    }}
    LIMIT 1
    '''.format(uri=movie.uri))
```

> [!WARNING]  
> Las consultas se construyen mediante una f-string en Python, por lo que para incluir llaves (`{` y `}`) en la consulta deberemos escaparlas usando una doble llave (`{{` y `}}`, respectivamente).

Para generar el nuevo fichero seeder de películas, es necesario generar una consulta que devuelva la información necesaria para el seed: título, imagen, lista de actores, director(es), fecha de estreno, etc.
Para esta tarea, se recomienda generar un fichero `generar_seeder.py` que genere una lista de películas haciendo varias consultas SPARQL a wikidata.

Por último, para descargar la información necesaria para generar `movies.ttl` tenemos varias alternativas:

* Descargar toda la información de cada película usando wikidata. Esta es la opción más sencilla, pero incluye información que puede no interesarnos.
* Utilizar `rdflib` para construir un grafo y añadir las triplas necesarias usando consultas SPARQL a wikipedia para cada una de las películas. Esta es la opción más flexible, pero requiere utilizar rdflib y un pequeño código python.
* Utilizar una única consulta SPARQL `CONSTRUCT`, que devuelve el resultado como un grafo (p.e., `ttl`). Esta es la opción más rápida, pero requiere tener un buen dominio de SPARQL para generar una única consulta SPARQL.
* Utilizar una consulta `CONSTRUCT` para cada película y unir los resultados


### create_review()

**Descripción:**  Crea una review de una película, primero se debe obtener la película dado su movie_slug y luego añadir la review.

**Parametros:** movie_slug, user_id, username, comment, rating

**Returns:** Un objeto movie con la review creada.

### 5.3 Añadir un marcador a la vista de Movies que indique si una película es favorita.

Se debe añadir en la vista de movies `static/templates/movies/show.html` un marcador en forma de imagen que indique que si esa película está marcada como favorita.

### 5.4 Manejo de Concurrencia.

En este apartado se plantean las tareas que van a permitir manejar la concurrencia para esta aplicación.

> [!WARNING]  
> Este apartado estará disponible cuando se haya cubierto el tema de concurrencia en clase.


## 6. Instrucciones para la Entrega y Evaluación.

> [!NOTE]  
> Se han includo una suite de tests para determinar si se han implementado de forma correcta cada una de las funciones y obtener una nota orientativa de acuerdo a la rúbrica.

Para poder ejecutar los tests debe ejecutar el siguiente comando:

```
python -m pytest -v --disable-warnings
```
Y obtendrá una salida similar a la siguiente:

```
================================== test session starts ===================================
platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0 -- /Users/admin/PX_ODM_FLASK/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/admin/PX_ODM_FLASK
plugins: harvest-1.10.4, mocha-0.4.0
collected 11 items                                                                       

flaskr/tests/test_check.py::test_list_movies PASSED                              [ 10%]
flaskr/tests/test_check.py::test_list_movies_by_filter PASSED                    [ 20%]
flaskr/tests/test_check.py::test_list_users PASSED                               [ 30%]
flaskr/tests/test_check.py::test_read_user PASSED                                [ 40%]
flaskr/tests/test_check.py::test_create_user PASSED                              [ 50%]
flaskr/tests/test_check.py::test_update_user PASSED                              [ 60%]
flaskr/tests/test_check.py::test_add_favorite_movie_to_user PASSED               [ 70%]
flaskr/tests/test_check.py::test_remove_favorite_movie_from_user PASSED          [ 80%]
flaskr/tests/test_check.py::test_create_review PASSED                            [ 90%]
flaskr/tests/test_check.py::test_show_score

La nota orientativa obtenida en la práctica es:


-----------------
| Score: 8.0 /8.0|
-----------------


PASSED                                 [100%]

============================ 11 passed, 47 warnings in 1.08s =============================

```

**RÚBRICA**: Cada método que se pide resolver de la practica se puntuará de la siguiente manera:
-  **0.5 puntos por crear los Modelos solicitados en el punto 5.1**
-  **0.5 puntos por añadir la imagen de favoritos a la vista de la película, lo indicado en el punto 5.3**
-  **1 punto** por capturar la información adecuada en la Consulta SPARQL en `read_movie()`.
-  **0.5 puntos por cada uno de las siguientes funciones realizadas:**  `list_movies_by_filter`, `list_users` y `read_user`
-  **1 puntos por cada uno de las siguientes funciones realizadas:**   `create_user` y `update_user`
-  **1.5 puntos** por la función `add_favorite_movie_to_user`, `remove_favorite_movie_from_user` y `create_review`.
