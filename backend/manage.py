from flask.cli import FlaskGroup
from app import create_app, db
from app.models import User, Department

app = create_app()
cli = FlaskGroup(create_app=lambda: app)

if __name__ == "__main__":
    cli()
