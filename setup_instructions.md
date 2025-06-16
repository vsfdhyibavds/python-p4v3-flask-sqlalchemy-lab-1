# Setup and Migration Instructions

## 1. Activate Python Environment and Install Dependencies

If you are using a virtual environment, activate it first. For example:

```bash
source venv/bin/activate
```

If you are using Pipenv:

```bash
pipenv shell
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

or if using Pipenv:

```bash
pipenv install
```

## 2. Run Database Migrations

Run the following commands to initialize and apply migrations:

```bash
python manage.py db init
python manage.py db migrate -m "Initial migration"
python manage.py db upgrade
```

## 3. Run Seed Script

After migrations are applied, run the seed script:

```bash
python server/seed.py
```

## 4. Run the Flask App

Start the Flask app:

```bash
python server/app.py
```

## 5. Test the App

Use a browser or curl to test the root endpoint:

```bash
curl http://localhost:5555/
```

You should see:

```json
{"message": "Flask SQLAlchemy Lab 1"}
```

---

If you encounter any issues during these steps, please let me know.
