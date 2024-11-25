from models import User
import datetime
from bson import ObjectId
import uuid
from flask import request

# Al empezar debes descomentar el código, se sigueire ir descomentando función por función para que no de error

""" def read_users():
    print("Obteniendo todos los users...")
    #Completar la función


    return users

def read_user(username):
    print("Obteniendo el user...", username)
    user = User.objects(username=username).first()
    return user

def create_user(username, name, surname, email, password_hash):
    print("Creando usuario...", username)
    #Completar la función

    
    return user

def update_user(username, name, surname, email, password_hash, country, city):
    print("Actualizando usuario...", username)
    #Completar la función

    
    return user

def add_favorite_movie_to_user(username, movie_id, movie_title, movie_slug):
    print("Añadiendo película favorita al usuario...", username)
    #Completar la función

    
    return user

def remove_favorite_movie_from_user(username, movie_id):
    print("Quitando película favorita al usuario...", username)
    #Completar la función

    
    return user """