from app import create_app, db
from app.models import Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Creates a shell context that adds the databse instance and models to the shell session"""
    return {"db": db, "Post": Post}
