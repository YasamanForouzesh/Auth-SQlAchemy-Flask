# Flask:
* run ```virtualenv venv or python -m virtualenv venv```
* active venv(Windows): ```source venv/Scripts/activate```
* ##### It's better install everything globally
* Install Flask: pip3 install flask
* import the Flask module from the pip flask library: from flask import Flask
* app = Flask(__name__)
##### what is the name of ``` @ ``` ?
###### decorator
##### resource for this one to get idea what does it do ?
* https://www.python.org/dev/peps/pep-0318/
# Auth (TOken or session)
##### Quick start for session:
* from flaskext.auth import Auth
* auth = Auth(app)

# SQLAlchemy
* Installing : 
* pip3 install SQLAlchemy
* pip install flask-sqlalchemy
* pip install psycopg2
* for each Table that we want to have in dataBase is going to be one class in models.py file
* from flask_sqlalchemy import SQLAlchemy
* db = SQLAlchemy(app)
* class Flight(db.Model) => it means Flight is inheretend of db.Model
* define foreign key: flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
* to create all tabels:  db.create_all()
* ```__tablename__ = "flights"```
* id = db.Column(db.Integer, primary_key=True)
* app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost:postgresport(5432)/databseName"
* You should create db manually
* write  python commend on your terminal to open the python shell
* ```>>> from models import db```
* ```>>> db.create_all()```
* os ?
* csv?
### query:
* python user = User(firstname="Yasaman",    lastname="Forouzesh",username="Yasi-f",password="pasword")
    db.session.add(user)
    db.session.commit() 
* ``` SELECT * FROM flights; ==  Flight.query.all() ```
* ``` SELECT * FROM flights WHERE origin = 'Paris' == Flight.query.filter_by(Origin = 'Paris').all() ```
# MongoAlchemy
# Auth:
## Token:

## Session:
## Bcrypt:
* install : pip3 install Bcrypt-Flask
* ``` from flask_bcrypt import Bcrypt ```
* ``` bcrypt = Bcrypt(app) ```
* ```   pw_hash = bcrypt.generate_password_hash(lastname=data.get("password")).decode('utf-8')```
# Run Flask app(Windows):
* $env:FLASK_APP = "app.py" 
* $python3 -m flask run
#  postgres commend for windows:
* login: psql -U postgres
* to see database : \l
* CREATE DATABASE tutorialdb;
* connect to db :  \c DBName;
* DROP DATABASE tutorialdb;

# Variable enviroment:
* pip install python-dotenv
* touch .env
# Hints:
* pip3 is for python3 package manager
* If you want to have pip file and pip shell to see all packages install : pip3 install pipenv
* pipenv shell
# Errors:
* from flask_sqlalchemy import SQLAlchemy ModuleNotFoundError: No module name 'flask_sqlalchemy' :
If you have another version of python, you should uninstall all other version. Sometime you should unistall everything and then install it.
* If you bcrypt your code but it saves different in your db add length to your password and decode your hash so add ``` .decode('utf-8') ``` end of your hash code.


# Resources:
* https://www.youtube.com/watch?v=PJK950Gp780
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
* https://www.youtube.com/watch?v=iIhAfX4iek0
* https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
* for cloudinery : https://medium.com/@johndavidsimmons/cloudinary-api-in-flask-14018d84a314