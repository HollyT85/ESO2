# ESO2

Django web application project

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser (optional):
```bash
python manage.py createsuperuser
```

## Project Structure

```
ESO2/
├── ESO/                # Django project configuration
│   ├── __init__.py
│   ├── settings.py     # Project settings
│   ├── urls.py         # URL routing
│   ├── wsgi.py         # WSGI config
│   └── asgi.py         # ASGI config
├── main/               # Django app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/          # HTML templates
│   ├── base.html
│   └── index.html
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── venv/               # Virtual environment (not committed)
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database
└── requirements.txt
```

## Running the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Common Django Commands

```bash
# Create new app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```
