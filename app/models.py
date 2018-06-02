from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artistname = db.Column(db.String(100), index=True, unique=True)
    artistlogo = db.Column(db.String(400))

    albums = db.relationship('Album', backref='artist', lazy='dynamic')

    def __repr__(self):
        return '<Artist {}>'.format(self.artistname)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    albumname = db.Column(db.String(100), index=True, unique=True)
    albumlogo = db.Column(db.String(400))
    albumlink = db.Column(db.String(500))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

    songs = db.relationship('Song', backref='album', lazy='dynamic')

    def __repr__(self):
        return'<Album {}>'.format(self.albumname)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.String(100), index=True)
    songlink = db.Column(db.String(500))
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))