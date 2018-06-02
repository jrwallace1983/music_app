from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ArtistForm(FlaskForm):
    artistname = StringField('Artist Name', validators=[DataRequired()])
    artistlogo = StringField('Artist Logo', validators=[DataRequired()])
    submit = SubmitField('Submit Artist')

class AlbumForm(FlaskForm):
    albumname = StringField('Album Name', validators=[DataRequired()])
    albumlogo = StringField('Album Logo', validators=[DataRequired()])
    albumlink = StringField('Album Video Link')
    submit = SubmitField('Submit Artist')

class SongForm(FlaskForm):
    songname = StringField('Song Name', validators=[DataRequired()])
    songlink = StringField('Song Video Link')