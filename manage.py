from server.app import app, migrate
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
