import os
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

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://{user}:{password}@netflix.ct6oxwoiakb5.us-east-2.rds.amazonaws.com:5432/netflix'
app = Flask(__name__)
#################################################
# Database Setup
#################################################
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine=engine, reflect=True)

db = SQLAlchemy(app)

# TODO: new table references

# Sites = create_classes_site(db)
# County = create_classes_county(db)
# CensusPopulation = create_classes_pop(db)
# year = create_classes_year(db)
# DateYear = create_classes_dateyear(db)
# Defining_Parameter = create_classes_def_param(db)
# AirQuality = create_classes_year(db)


# # API KEY on HEROKU
# from boto.s3.connection import S3Connection
# s3 = S3Connection(os.environ['API_KEY'], os.environ['API_KEY_SECRET'])
# API_KEY = app.config['API_KEY']


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
    
# @app.route("/timelapse")
# def timelapse():
#     details = get_timelapse()
#     return render_template(
#         'timelapse.html',
#         map_id = details[0],
#         hdr_txt=details[1],
#         script_txt = details[2]
#     )

if __name__ == '__main__':
    app.run(debug=True)

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
