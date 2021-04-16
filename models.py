from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
#add base
Base = declarative_base()
import sys

class Netflix_Listed_in(Base):
    __tablename__ = 'Netflix_Listed_in'
    netflix_genre_no = Column(Integer, primary_key=True)
    netflix_genre = Column(String)

    def serialize(self):
            return {
                "netflix_genre_no" : self.netflix_genre_no,
                "netflix_genre" : self.netflix_genre
            }

class OMDB_genre(Base):
    __tablename__ = 'OMDB_genre'
    omdb_genre_no = Column(Integer, primary_key=True)
    omdb_genre = Column(String)

    def serialize(self):
        return {
            "omdb_genre_no" : self.omdb_genre_no,
            "omdb_genre" : self.omdb_genre
        }

class OMDB_language(Base):
    __tablename__ = 'OMDB_language'
    language_no = Column(Integer, primary_key=True)
    language = Column(String)

    def serialize(self):
        return {
            "omdb_genre_no" : self.omdb_genre_no,
            "omdb_genre" : self.omdb_genre
        }


class Title(Base):
    __tablename__ = 'Title'
    show_id = Column(Integer, primary_key=True)
    type = Column(String)
    title = Column(String)
    director = Column(String)
    cast = Column(String)
    country = Column(String)
    date_added = Column(String)
    release_year = Column(Integer)
    rating = Column(String)
    duration = Column(String)
    description = Column(String)
    runtime = Column(String)
    imdbRating = Column(Float)
    imdbVotes = Column(Integer)
    poster = Column(String)
    awards = Column(String)
    boxoffice = Column(String)

    def serialize(self):
        return {
            "show_id" : self.show_id,
            "type" : self.type,
            "title" : self.title,
            "director" : self.director,
            "cast" : self.cast,
            "country" : self.country,
            "date_added" : self.date_added,
            "release_year" : self.release_year,
            "rating" : self.rating,
            "duration" : self.duration,
            "description" : self.description,
            "runtime" : self.runtime,
            "imdbRating" : self.imdbRating,
            "imdbVotes" : self.imdbVotes,
            "poster" : self.poster,
            "awards" : self.awards,
            "boxoffice" : self.boxoffice
        }

class Netflix_title_Listed_in(Base):
    __tablename__ = 'Netflix_title_Listed_in'
    netflix_genre_no = Column(Integer, primary_key=True)
    show_id = Column(Integer, primary_key=True)

    def serialize(self):
        return {
            "netflix_genre_no" : self.netflix_genre_no,
            "show_id" : self.show_id
        }


class OMDB_title_language(Base):
    __tablename__ = 'OMDB_title_language'
    language_no = Column(Integer, primary_key=True)
    show_id = Column(Integer, primary_key=True)

    def serialize(self):
        return {
            "language_no" : self.language_no,
            "show_id" : self.show_id
        }

class OMDB_title_genre(Base):
    __tablename__ = 'OMDB_title_genre'
    omdb_genre_no = Column(Integer, primary_key=True)
    show_id = Column(Integer, primary_key=True)

    def serialize(self):
        return {
            "omdb_genre_no" : self.omdb_genre_no,
            "show_id" : self.show_id
        }

class Cast(Base):
    __tablename__ = 'cast'
    cast_no = Column(Integer, primary_key=True)
    cast = Column(String)
    children = relationship("Title_cast", back_populates="cast")

    def serialize(self):
        return {
            "cast_no" : self.cast_no,
            "cast" : self.cast
        }

class Title_cast(Base):
    __tablename__ = 'title_cast'
    show_id = Column(Integer, primary_key=True)
    cast_no = Column(Integer, ForeignKey('cast.cast_no'))
    cast = relationship("Cast", back_populates="children")
    
    def serialize(self):
        return {
            "cast_no" : self.cast_no,
            "show_id" : self.show_id,
            "cast" : self.cast
        }




        
