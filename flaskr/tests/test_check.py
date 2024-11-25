import pytest
from flask import Flask
from bson import ObjectId
import controllers.movieController as movieController
import controllers.userController as userController
from flask_mongoengine import MongoEngine
from tests.helper import seeder

score = 0
# Metodo para pre-tests, se ejecuta el inicio de cada test
# Crea la bbdd db_test la llena con los seeders y luego de ejeuctar el test borra la bbdd
@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    from flask_mongoengine import MongoEngine
    app = Flask("test_data")
    db = MongoEngine()
    db.disconnect(alias='default')
    app.config["MONGODB_SETTINGS"] = {
            "db": "db_test",
            "host": "mongodb://localhost/db_test",
            "port": 27017,
            "alias": "default",
    }
    db.init_app(app)
    db_name = db.get_db().name
    seeder(app)


    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    db_collections_size = len(db.get_db().list_collection_names())
    assert db_name == "db_test"
    assert db_collections_size is 2

    # Confirmo con MongoEngine que la bbdd ha sido borrada    
    from mongoengine import connect
    db.disconnect(alias='default')
    db = connect(db_name)
    db.drop_database(db_name)
    db_collections_size= len(db.get_database(db_name).list_collection_names())
    assert db_collections_size is 0


def test_list_movies():
    all_movies = movieController.read_movies()
    assert len(all_movies) == 5
    assert all_movies[0].id == ObjectId("670e6fe1a5e24a431c1e6800")
    assert all_movies[1].id == ObjectId("670e6fe1a5e24a431c1e6807")
    assert all_movies[2].id == ObjectId("670e6fe1a5e24a431c1e680b")
    assert all_movies[3].id == ObjectId("670e6fe1a5e24a431c1e6812")
    assert all_movies[4].id == ObjectId("670e6fe1a5e24a431c1e6817")

def test_list_movies_by_filter():
    title = "Forrest"
    genre = "Drama"
    director = "D"
    all_movies = movieController.read_movies_by_filter(title, None, None )
    assert len(all_movies) == 1
    all_movies = movieController.read_movies_by_filter(None, genre, None)
    assert len(all_movies) == 4
    all_movies = movieController.read_movies_by_filter(None, None, director )
    assert len(all_movies) == 3
    global score; score += 0.5 # Increase score

""" def test_read_movie():
    slug = "forrest-gump"
    movie = movieController.read_movie(slug)
    assert movie.id == ObjectId("670e6fe1a5e24a431c1e6807")
    global score; score += 1.5 # Increase score """


def test_list_users():  
    all_users = userController.read_users()
    assert len(all_users) == 5
    assert all_users[0].id == ObjectId("670d392bd5c2c5162183667f")
    assert all_users[1].id == ObjectId("670d392bd5c2c51621836680")
    assert all_users[2].id == ObjectId("670d392bd5c2c51621836681")
    assert all_users[3].id == ObjectId("670d392bd5c2c51621836682")
    assert all_users[4].id == ObjectId("670d392bd5c2c51621836683")
    global score; score += 0.5 # Increase score

def test_read_user():
    username = "user1"
    user = userController.read_user(username)
    assert user.id == ObjectId("670d392bd5c2c51621836680")
    assert user.username == "user1"
    assert user.name == "Pepe"
    assert user.surname == "Pérez"
    assert user.email == "user1@example.com"
    assert user.password_hash == "pbkdf2:sha256:600000$zLAf9wteFz2oPXgF$684b1c08edaaaa892f7ab5a589a2689bb43198edaa372cad4818ed0916e93b4a"
    assert user.country == "Spain"
    assert user.city == "Madrid"
    global score; score += 0.5 # Increase score

def test_create_user():
    user_data = {
       "username": "jwick",
       "name":"John",
       "surname": "Wick",
       "email": "jwick@example.com",
        "password_hash": "pbkdf2:sha256:600000$zLAf9wteFz2oEXgF$684b1c08edaaaa892f7ab5a589a2689bb43198edaa312cad4818ed0916e93b4a",
        "country": "Germany",
        "city": "Munich"
    }
    print(user_data)

    created_user = userController.create_user(user_data["username"], user_data["name"], user_data["surname"], user_data["email"], user_data["password_hash"])
    assert created_user.username == "jwick"
    assert created_user.name == "John"
    assert created_user.surname == "Wick"
    assert created_user.password_hash == "pbkdf2:sha256:600000$zLAf9wteFz2oEXgF$684b1c08edaaaa892f7ab5a589a2689bb43198edaa312cad4818ed0916e93b4a"
    assert created_user.email == "jwick@example.com"
    global score; score += 1 # Increase score

def test_update_user():

    user_data = {
       "id": ObjectId("670d392bd5c2c51621836681"),
       "username":"john",
       "name":"John",
       "surname": "Doe",
       "email": "jodoe@example.com",
       "password_hash": "pbkdf2:sha256:600000$zLAf9wteFz2oEXgF$684b1c08edaaaa892f7ab5a589a2689bb43198edaa312cad4818ed0916e93b4a",
       "country": "Germany",
       "city": "Berlin"
    }
    updated_user=userController.update_user(user_data["username"],user_data["name"],user_data["surname"],user_data["email"],user_data["password_hash"],user_data["country"],user_data["city"])
    assert updated_user.id == user_data["id"]
    assert updated_user.username == user_data["username"]
    assert updated_user.name == user_data["name"]
    assert updated_user.surname == user_data["surname"]
    assert updated_user.email == user_data["email"]
    assert updated_user.password_hash == user_data["password_hash"]
    assert updated_user.country == user_data["country"]
    assert updated_user.city == user_data["city"]
    global score; score += 1 # Increase score

def test_add_favorite_movie_to_user():
    user_username = "john"
    movie_id = ObjectId("670e6fe1a5e24a431c1e6807")
    movie_title = "Forrest Gump"
    movie_slug = "forrest-gump"
    favorite_user = userController.add_favorite_movie_to_user(user_username, movie_id, movie_title, movie_slug)
    assert favorite_user.username == user_username
    assert favorite_user.favorite_movies[2]["_id"] == movie_id
    assert favorite_user.favorite_movies[2]["title"]== movie_title
    assert favorite_user.favorite_movies[2]["slug"] == movie_slug
    global score; score += 1.5 # Increase score

def test_remove_favorite_movie_from_user():
    username = "john"
    movie_id = ObjectId("670e6fe1a5e24a431c1e6807")
    user = userController.remove_favorite_movie_from_user(username, movie_id)  
    assert len(user.favorite_movies) == 2
    assert user.favorite_movies[0]["_id"] == "670e6fe1a5e24a431c1e6800"
    assert user.favorite_movies[1]["_id"] == "670e6fe1a5e24a431c1e6801"
    global score; score += 1.5 # Increase score

def test_create_review():
    movie_slug= "forrest-gump"
    test_review = {
                "user_id": ObjectId("670d392bd5c2c51621836680")     ,
                "username": "user1",
                "rating": 10,
                "comment": "Inspiradora y conmovedora."
            }
    movie_with_review = movieController.create_review(movie_slug, test_review["user_id"],test_review["username"], test_review["comment"], test_review["rating"] )
    assert movie_with_review.reviews[len(movie_with_review.reviews)-1].username == test_review["username"]
    assert movie_with_review.reviews[len(movie_with_review.reviews)-1].rating == test_review["rating"]
    assert movie_with_review.reviews[len(movie_with_review.reviews)-1].comment == test_review["comment"]
    global score; score += 1.5 # Increase score


    
def test_show_score(capsys):
    with capsys.disabled():
        print('\n\nLa nota orientativa obtenida en la práctica es:')
        print('\n\n-----------------')
        print('| Score: {} /8.0|'.format(score))
        print('-----------------\n')