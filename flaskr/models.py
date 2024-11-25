from db import db

class User(db.Document):
    #_id es the objectId asignado por mongo
   
    #el username tiene que ser único porque lo usamos para las rutas /users/<username>
    
    #favorite_movies es un array de objetos con dos valores, el id de la película, el título y el slug
    
    updated_at = db.DateTimeField()

# Subdocumento para los Actores
class Actor(db.EmbeddedDocument):
    name = db.StringField(required=True)
    date_of_birth = db.StringField()
    biography = db.StringField()
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

# Subdocumento para las reseñas
class Review(db.EmbeddedDocument):
    user_id = db.ReferenceField(User)
    username = db.StringField(required=True)
    rating = db.IntField(min_value=1, max_value=10)
    comment = db.StringField()

# Modelo de Películas
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
    reviews = db.ListField(db.EmbeddedDocumentField(Review))
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

