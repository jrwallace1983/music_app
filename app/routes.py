from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.models import Artist, Album, Song
from app.forms import ArtistForm, AlbumForm, SongForm


@app.route('/music')
def music():
    artist = Artist.query.order_by().all()
    return render_template('music.html', title='Music', artist=artist)

@app.route('/enterartist', methods=['GET', 'POST'])
def enterartist():
    form = ArtistForm()
    if form.validate_on_submit():
        artist = Artist(artistname=form.artistname.data, artistlogo=form.artistlogo.data)
        db.session.add(artist)
        db.session.commit()
        flash('You Submitted {}'.format(form.artistname.data))
        return redirect('/music')

    return render_template('enter_artist.html', title='Music', form=form)

@app.route('/artist/<int:artist_id>/', methods=['GET', 'POST'])
def album(artist_id):
    form = AlbumForm()
    album = Album.query.filter_by(artist_id=artist_id).all()
    artist = Artist.query.filter_by(id=artist_id).first()
    song = db.session.query(Album, Song).join(Song, Album.id==Song.album_id).filter(Album.artist_id==artist_id)
    youtube = Album.query.filter_by(artist_id=artist_id).first()
    if form.validate_on_submit():
        newalbum = Album(albumname=form.albumname.data, albumlogo=form.albumlogo.data, albumlink=form.albumlink.data, artist_id=artist_id)
        db.session.add(newalbum)
        db.session.commit()
        return redirect(url_for('music'))
    return render_template('artist.html', title='Artist', album=album, artist=artist, youtube=youtube, form=form, song=song)

'''def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=_('Register'),
                           form=form)'''