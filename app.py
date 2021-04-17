import os
from typing import cast
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template_string,
    render_template,
    jsonify,
    request,
    redirect,
    send_from_directory)
import numpy as np
from flask_cors import CORS
#from config import username, password
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sys
from models import *

##Imports used for Machine Learning##
import nltk
import re
import pickle
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


#import boto3

#SQLALCHEMY_DATABASE_URI = os.getenv('THE_BIG_CHILL_DATABASE_URL') 
SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://roo2:123456@netflix.cy8gt7mz64dd.us-east-2.rds.amazonaws.com:5432/postgres"

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

CORS(app)
#################################################
# Database Setup
#################################################
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# engine=create_engine(os.getenv('DATABASE_URL'))
conn=engine.connect()

#create tables
Base.metadata.create_all(conn)

# DATABASE_URL will contain the database connection string: HEROKU
# from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
def confg():
    engine = create_engine(
        "postgres+psycopg2://{username}:{password}@netflix.cy8gt7mz64dd.us-east-2.rds.amazonaws.com:5432/postgres")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    session = Session(engine)

    return Base,session


@app.route('/title', methods=['GET'])
def title():
    Base,session= confg()
    titles=Base.classes.Title
    title_sql=session.query(titles).all()
    list=[]
    for i in title_sql:
        feature_dict={}
        feature_dict["title"]=i.title
        feature_dict["rating"]=i.rating
        feature_dict["imdb_rating"]=i.imdbrating
        feature_dict["description"]=i.description
        feature_dict["type"]=i.type
        feature_dict["country"]=i.country
        feature_dict["poster"]=i.poster
        list.append(feature_dict)
    title_dict={}
    title_dict["netflix"]=list
    return title_dict



# @app.route('/index', methods=['GET', 'POST'])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/deep_dive")
def deep_dive():
    return render_template("deep_dive.html")

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

# Leftover code -- if we want these pages
@app.route("/about")
def members():
    return render_template("about.html")

@app.route("/test_db")
def test_db():
    # Create our session (link) from Python to the DB
    session = Session(bind=engine)
    
    cast_title_db = session.query(Title_cast).join(Cast, Cast.cast_no == Title_cast.cast_no).all()
    # cast_title_db = (session.query(title_cast, title_cast.cast_no, title_cast.show_id).outerjoin(cast, cast.cast_no == title_cast.cast_no))

    # Create a dictionary from the row data and append to a list 
    all_cast_title = []
    
    for i in cast_title_db:
     cast_title_no = {}
     cast_title_no["cast"] = i.cast
     cast_title_no["cast_no"] = i.show_id
     cast_title_no["show_id"] = i.show_id
     all_cast_title.append(cast_title_no)

     session.close()

    return jsonify(all_cast_title)



# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# def tmpl_show_menu():
#     return render_template_string(
#         """
#         {%- for item in current_menu.children %}
#             {% if item.active %}*{% endif %}{{ item.text }}
#         {% endfor -%}
#         """)

# @app.route('/')
# @register_menu(app, '.', 'Home')
# def index():
#     return tmpl_show_menu()

# @app.route('/first')
# @register_menu(app, '.first', 'First', order=0)
# def first():
#     return tmpl_show_menu()

# @app.route('/second')
# @register_menu(app, '.second', 'Second', order=1)
# def second():
#     return tmpl_show_menu()

###########################################
## Definitions used for Machine Learning ##
###########################################

##remove commonly used words that are not good for training
def remove_stopwords(text):
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)

def clean_text(text):
    # remove backslash-apostrophe 
    text = re.sub("\'", "", text) 
    # remove everything except alphabets 
    text = re.sub("[^a-zA-Z]"," ",text) 
    # remove whitespaces 
    text = ' '.join(text.split()) 
    # convert text to lowercase 
    text = text.lower() 
    return text

## clean user input and return prediction
def infer_tags(q):
    ##lower case and remove non alpha
    q = clean_text(q)
    ##remove junk words
    q = remove_stopwords(q)
    ##PREDICT
    q_pred = LogReg_pipeline.predict([q])
    ##convert prediction back to genre
    return multilabel_binarizer.inverse_transform(q_pred)

def infer_rating(q):
    q = clean_text(q)
    q = remove_stopwords(q)
    q_pred = LogRegRating_pipeline.predict([q])
    return multilabel_binarizer_rating.inverse_transform(q_pred)

## Load the trained model
with open('static/data/description_genre.pkl', 'rb') as f:
    multilabel_binarizer, LogReg_pipeline = pickle.load(f)
with open('static/data/description_rating.pkl', 'rb') as r:
    multilabel_binarizer_rating, LogRegRating_pipeline = pickle.load(r)

@app.route("/ML")
def machine_learning():
    plot = ""
    predictive_output = []
    #get user input 
    plot = request.args.get('plot', type = str)
    if plot != "":
         predictive_output_genres = infer_tags(plot)
         predictive_output.append(predictive_output_genres)
         ##uncomment this line if we get the descriptive ratings model working
         predictive_output_rating = infer_rating(plot)
         predictive_output.append(predictive_output_rating)
    else:
        return("No input found")     
    print(predictive_output)
    return jsonify(predictive_output)

  
if __name__ == '__main__':
    app.run(debug=True)