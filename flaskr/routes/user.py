from flask import Blueprint, request 
from controllers.userController import *
from flask import render_template, redirect
from flask import flash
from flask import g
from flask import session
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


userbp = Blueprint('user', __name__, template_folder='templates', url_prefix='/users')

@userbp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from the database into ``g.user``."""
    username = session.get("username")

    if username is None:
        g.user = None
    else:
        g.user = User.objects.get(username=username)
        

@userbp.route('/', methods=['GET'])
def show_users():
    print("Ruta '/' -> Index de users")
    return render_template('users/index.html', users=read_users())

@userbp.route('/<username>', methods=['GET'])
def show_user(username):
    username = request.args.get('name')
    print("Ruta '/<username>' -> Mostrar un user")
    print(username)
    return render_template('users/show.html', user=read_user(username))


@userbp.route('/', methods=['POST'])
def create_user_route():
    print("Ruta POST a '/' -> Crear un user")
    username = request.form['username']
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password_hash = generate_password_hash(request.form['password'])
    
    try:       
        #creates user in the database
        create_user(username, name, surname, email, password_hash)
    except Exception as e:
        print("Error al crear el usuario:", e)
        flash("Error al crear el usuario: " + str(e), "error")
        return redirect("/users")
    
    return redirect("/users")


@userbp.route('/<username>/edit', methods=['GET'])
def edit_user(username):
    print("Ruta '/<username>/edit' -> Editar un user")
    #comprobamos que el usuario es el que está logueado en
    if g.user is None:
        return redirect("/login")
    if g.user.username != username:
        flash("Ruta no permitida, debes estar logueado como el usuario que quieres editar", "error")
        return redirect("/movies")

    return render_template('users/edit.html', user=read_user(username))


@userbp.route('/<username>', methods=['POST'])
def update_user_route(username):
    print("Ruta POST a '/<username>' -> Actualizar un user")      
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password_hash = generate_password_hash(request.form['password'])
    country = request.form['country']
    city = request.form['city']

    print("Datos del formulario:", username, name, surname, email, password_hash, country, city)
    
    #updates user in the database
    update_user(username, name, surname, email, password_hash, country, city)
    
    return redirect("/users")

@userbp.route('/<username>/addfavorite', methods=['POST'])
def add_favorite_movie_route(username):
    print("Ruta POST a '/<username>/addfavorite' -> Añadir película a favoritos")
    movie_id = request.form['movie_id']
    movie_title = request.form['movie_title']
    movie_slug = request.form['movie_slug']
    
    try:       
        #adds favorite in the user list in the database
        add_favorite_movie_to_user(username, movie_id, movie_title, movie_slug)
    except Exception as e:
        print("Error al añadir la película a favoritos:", e)
        flash("Error al añadir la película a favoritos: " + str(e), "error")
        return redirect("/movies/"+movie_slug)
    
    flash("Película añadida a favoritos", "info")
    return redirect("/movies/"+movie_slug)

@userbp.route('/<username>/removefavorite', methods=['POST'])
def remove_favorite_movie_route(username):
    print("Ruta POST a '/<username>/removefavorite' -> Quitar película de favoritos")
    movie_id = request.form['movie_id']  
    movie_slug = request.form['movie_slug']
    
    try:       
        #removes favorite from the user list in the database
        remove_favorite_movie_from_user(username, movie_id)
    except Exception as e:
        print("Error al añadir la película a favoritos:", e)
        flash("Error al añadir la película a favoritos: " + str(e), "error")
        return redirect("/movies/"+movie_slug)
    
    flash("Película quitada de favoritos", "info")
    return redirect("/movies/"+movie_slug)