def create_classes(db):

    class Netflix_Listed_in(db.Model):
        __tablename__ = 'Netflix_Listed_in'

        netflix_genre_no = db.Column(db.Integer, primary_key=True)
        netflix_genre = db.Column(db.Varchar)

        def __repr__(self):
            return '<Netflix_Listed_in %r>' % (self.name)
    return Netflix_Listed_in

    class OMDB_genre(db.Model):
        __tablename__ = 'OMDB_genre'

        omdb_genre_no = db.Column(db.Integer, primary_key=True)
        omdb_genre = db.Column(db.Varchar)

        def __repr__(self):
            return '<OMDB_genre %r>' % (self.name)
    return OMDB_genre

    class OMDB_language(db.Model):
        __tablename__ = 'OMDB_language'

        language_no = db.Column(db.Integer, primary_key=True)
        language = db.Column(db.Varchar)

        def __repr__(self):
            return '<OMDB_language %r>' % (self.name)
    return OMDB_language

    class Title(db.Model):
        __tablename__ = 'Title'

        show_id = db.Column(db.Integer, primary_key=True)
        type = db.Column(db.Varchar)
        title = db.Column(db.Varchar)
        director = db.Column(db.Varchar)
        cast = db.Column(db.Varchar)
        country = db.Column(db.Varchar)
        date_added = db.Column(db.Varchar)
        release_year = db.Column(db.Integer)
        rating = db.Column(db.Varchar)
        duration = db.Column(db.Varchar)
        description = db.Column(db.Varchar)
        runtime = db.Column(db.Varchar)
        imdbRating = db.Column(db.Double)
        imdbVotes = db.Column(db.Integer)
        poster = db.Column(db.Varchar)
        awards = db.Column(db.Varchar)
        boxoffice = db.Column(db.Varchar)

        def __repr__(self):
            return '<Title %r>' % (self.name)
    return Title    

    class Cast(db.Model):
        __tablename__ = 'cast'

        cast_no = db.Column(db.Integer, primary_key=True)
        cast = db.Column(db.Varchar)

        def __repr__(self):
            return '<Cast %r>' % (self.name)
    return Cast

    class Netflix_title_Listed_in(db.Model):
        __tablename__ = 'Netflix_title_Listed_in'

        netflix_genre_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<Netflix_title_Listed_in %r>' % (self.name)
    return Netflix_title_Listed_in

    class OMDB_title_language(db.Model):
        __tablename__ = 'OMDB_title_language'

        language_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<OMDB_title_language %r>' % (self.name)
    return OMDB_title_language

    class OMDB_title_genre(db.Model):
        __tablename__ = 'OMDB_title_genre'

        omdb_genre_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<OMDB_title_genre %r>' % (self.name)
    return OMDB_title_genre

    class title_cast(db.Model):
        __tablename__ = 'title_cast'

        cast_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<title_cast %r>' % (self.name)
    return title_cast




        
