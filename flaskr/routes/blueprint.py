from flask import Blueprint, request 
from controllers.movieController import *
from controllers.userController import *
from flask import render_template, redirect
from flask import flash
from flask import session
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


generalbp = Blueprint('general', __name__, template_folder='templates', url_prefix='/')

@generalbp.route('/', methods=['GET'])
def index():
    print("ruta '/' -> Redirigiendo a /movies, Index de movies")
    #redirect to the movies index
    return redirect('/movies')
    
    
@generalbp.route('/login', methods=['GET'])
def get_login_form():
    print("Ruta '/login' -> Formulario de login")
    return render_template('users/login.html')


@generalbp.route('/login', methods=['POST'])
def login_user():
    print("Ruta POST a '/login' -> Login de usuario")
    username = request.form['username']
    password = request.form['password']
    user = read_user(username)
    if user is None:
        error = "Username no existe."
    elif not check_password_hash(user["password_hash"], password):
        error = "Password incorrecto."
    else:
        error = None
    
    if error is None:
        # store the user username in a new session and return to the index
        session.clear()
        session["username"] = user["username"]
        return redirect(f"/users/{username}")
    
    flash(error, "error")
    return redirect("/login")


@generalbp.route('/logout', methods=['GET'])
def logout():
    print("Ruta '/logout' -> Logout de usuario")
    session.clear()
    return redirect("/")


@generalbp.route('/register', methods=['GET'])
def register_user():
    print("Ruta '/register' -> Formulario de registro")
    return render_template('users/register.html')