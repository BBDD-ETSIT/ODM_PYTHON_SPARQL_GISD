from flask import Blueprint, request 
from controllers.movieController import *
from flask import render_template, redirect
from flask import flash
from flask import g
from flask import session


moviebp = Blueprint('movie', __name__, template_folder='templates', url_prefix='/movies')

@moviebp.route('/', methods=['GET'])
def index():
    print("ruta '/' -> Index de películas")
    return render_template('movies/index.html', movies=read_movies())

@moviebp.route('/movies_filtered', methods=['GET'])
def movies_filtered():
    print("ruta '/movies_filtered' -> Index de películas")
    title = request.args.get('title')
    genre = request.args.get('genre')
    director = request.args.get('director')
    return render_template('movies/index.html', movies=read_movies_by_filter(title=title,genre=genre, director=director))


@moviebp.route('/<slug>', methods=['GET'])
def show(slug):
    print("ruta '/<movie_slug>' -> Mostrar una película")
    return render_template('movies/show.html', movie=read_movie(slug))


@moviebp.route('/<slug>/comments', methods=['POST'])
def create_comment_route(slug):
    print("ruta POST a '/<movie_slug>/comments' -> Crear un comentario")
    user_id = g.user._id
    username = g.user.username
    comment = request.form['comment']
    rating = request.form['rating']
    
    try:       
        #creates user in the database
        create_review(slug, user_id, username, comment, rating)
    except Exception as e:
        print("Error al crear el comentario:", e)
        flash("Error al crear el comentario: " + str(e), "error")
        return redirect("/movies/"+slug)
    
    return redirect("/movies/"+slug)