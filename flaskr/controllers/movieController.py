from models import Movie
from models import Review
from sparql import query
from flask import g, request


def read_movies():
    print("Reading movies...")
    movies = Movie.objects()
    print("aaaa")
    print(movies)
    print("bbb")
    
    return movies

def read_movies_by_filter(title, genre, director):
    #Completar la función
    movies = ""

    
    return movies


def read_movie(slug):
    print("Reading movie...", slug)
    #Completar la función
    movie = ""
    
    return movie


def create_review(movie_slug, user_id, username, comment, rating):
    print("Creating review...", movie_slug)
    #Completar la función
    movie = ""
    
    return movie 
