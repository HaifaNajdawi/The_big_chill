import os
# import psycopg2
from flask import Flask
from flask import render_template_string
from flask import render_template
from sqlalchemy import create_engine

app = Flask(__name__)
# # Menu(app=app)

# # DATABASE_URL will contain the database connection string: HEROKU
#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/Netflix_movies"
engine = create_engine(f'postgresql://{rds_connection_string}')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Connects to the database using the app config
# db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model")
def countryvpop():
    return render_template("countyvpop.html")

if __name__ == '__main__':
    app.run(debug=True)