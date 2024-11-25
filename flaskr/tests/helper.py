# encoding: utf-8

from models import User, Movie
from db import db
from datetime import datetime
from dateutil import parser 
import json
import os


################### Espacio para seeders ############################

# método que comprueba si estamos conectados a la base de datos y si hay hospitales, si no los añade de seeders/seeders.json
def seeder(app):
    print('#### METODO SEEDER ####')
    with app.app_context():
        db_name = db.get_db().name
        if(db_name):
            print('#### Database exist with name: '+ db_name +' ####')
        else:
            print('#### Database not exist ####')


    all_movies = Movie.objects.all()
    all_users = User.objects.all()

    if (len(all_movies) <= 0):
        print('#### Movie collection is empty ####')
        print('#### Adding some entries... ####')
        with open(os.path.join(os.path.dirname(__file__), './test_seeders/movie.json'), 'r', encoding='utf-8') as f:
            print('#### seeders.json file opened... ---####')
            movies = json.load(f)

        for movie in movies:
            new_movie = Movie(**movie)
            new_movie.save()

        print('#### Finished! ####')
    else:
        print('#### Movie collection already seeded ####')

    if (len(all_users) <= 0):
        print('#### User collection is empty ####')
        print('#### Adding some entries... ####')
        with open(os.path.join(os.path.dirname(__file__), './test_seeders/user.json'), 'r', encoding='utf-8') as f:
            print('#### seeders.json file opened... ---####')
            users = json.load(f)
    
        for user in users:
            
            """ user['created_at'] = parser.parse(user['created_at'])
            user['updated_at'] = parser.parse(user['updated_at']) """
            new_user = User(**user)
            
            print(new_user.created_at)
            new_user.save()
    else:
        print('#### User collection already seeded ####')

