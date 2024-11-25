from routes.user import userbp
from routes.movie import moviebp
from routes.blueprint import generalbp

from db import db, app


def create_app():
    db.init_app(app)  # Initializing the database
    return app

app = create_app()  # Creating the app


# Registering the blueprint
app.register_blueprint(userbp)
app.register_blueprint(moviebp) 
app.register_blueprint(generalbp)
