import os
import tempfile
import pytest
from server.app import app, db

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_app_root(client):
    """Test the root endpoint returns the expected message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Flask SQLAlchemy Lab 1'}

def test_database_initialization(client):
    """Test that the database tables are created."""
    with app.app_context():
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        assert 'earthquake' in tables or 'earthquake' in [t.lower() for t in tables]
