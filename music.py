from app import app, db
from app.models import Artist, Album, Song

@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'Artist': Artist, 'Album': Album, 'Song': Song}