def create_classes_netflix_listed_in(db):
    class Netflix_Listed_in(db.Model):
        __tablename__ = 'Netflix_Listed_in'

        netflix_genre_no = db.Column(db.Integer, primary_key=True)
        netflix_genre = db.Column(db.String)

        def __repr__(self):
            return '<Netflix_Listed_in %r>' % (self.name)
    return Netflix_Listed_in

def create_classes_OMDB_genre(db):
    class OMDB_genre(db.Model):
        __tablename__ = 'OMDB_genre'

        omdb_genre_no = db.Column(db.Integer, primary_key=True)
        omdb_genre = db.Column(db.String)

        def __repr__(self):
            return '<OMDB_genre %r>' % (self.name)
    return OMDB_genre

def create_classes_OMDB_language(db):
    class OMDB_language(db.Model):
        __tablename__ = 'OMDB_language'

        language_no = db.Column(db.Integer, primary_key=True)
        language = db.Column(db.String)

        def __repr__(self):
            return '<OMDB_language %r>' % (self.name)
    return OMDB_language

def create_classes_title(db):
    class Title(db.Model):
        __tablename__ = 'Title'

        show_id = db.Column(db.Integer, primary_key=True)
        type = db.Column(db.String)
        title = db.Column(db.String)
        director = db.Column(db.String)
        cast = db.Column(db.String)
        country = db.Column(db.String)
        date_added = db.Column(db.String)
        release_year = db.Column(db.Integer)
        rating = db.Column(db.String)
        duration = db.Column(db.String)
        description = db.Column(db.String)
        runtime = db.Column(db.String)
        imdbRating = db.Column(db.Float)
        imdbVotes = db.Column(db.Integer)
        poster = db.Column(db.String)
        awards = db.Column(db.String)
        boxoffice = db.Column(db.String)

        def __repr__(self):
            return '<Title %r>' % (self.name)
    return Title    

def create_classes_cast(db):
    class Cast(db.Model):
        __tablename__ = 'cast'

        cast_no = db.Column(db.Integer, primary_key=True)
        cast = db.Column(db.String)

        def __repr__(self):
            return '<Cast %r>' % (self.name)
    return Cast

def create_classes_netflix_title_listed_in(db):
    class Netflix_title_Listed_in(db.Model):
        __tablename__ = 'Netflix_title_Listed_in'

        netflix_genre_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<Netflix_title_Listed_in %r>' % (self.name)
    return Netflix_title_Listed_in

def create_classes_OMDB_title_language(db):
    class OMDB_title_language(db.Model):
        __tablename__ = 'OMDB_title_language'

        language_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<OMDB_title_language %r>' % (self.name)
    return OMDB_title_language

def create_classes_OMDB_title_genre(db):
    class OMDB_title_genre(db.Model):
        __tablename__ = 'OMDB_title_genre'

        omdb_genre_no = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<OMDB_title_genre %r>' % (self.name)
    return OMDB_title_genre

def create_classes_title_cast(db):
    class title_cast(db.Model):
        __tablename__ = 'title_cast'

        cast_no = db.Column(db.Integer, primary_key=True)
        # cast = db.relationship('Cast', backref = 'cast',cascade='all, delete, delete-orphan',single_parent=True)
        show_id = db.Column(db.Integer, primary_key=True)

        def __repr__(self):
            return '<title_cast %r>' % (self.name)
    return title_cast




        
