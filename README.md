# Travel Management System

A Django web application for browsing travel destinations, submitting a hotel
booking, and displaying a payment confirmation.

## Features

- Destination catalogue with travel imagery and detail pages
- Booking form for a traveller, destination, date, and hotel
- Fixed per-destination package pricing
- Django admin views for bookings and payments

## Project layout

```text
myproject/          Django project configuration
myapp/              Booking models, views, routes, templates, and admin
static/             Source CSS, JavaScript, and images
assets/             Project presentation and logo files
requirements.txt    Python dependencies
```

## Local setup

Requires Python 3.10 or later.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

To create an administrator account:

```powershell
python manage.py createsuperuser
```

Visit <http://127.0.0.1:8000/admin/> to sign in.

## Common commands

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test
```

## Repository conventions

- Commit source code, templates, migrations, and intentional static assets.
- Do not commit `.venv/`, `Test/`, `db.sqlite3`, `staticfiles/`, or `.env` files.
- Keep secrets such as `SECRET_KEY` and production settings in environment
  variables before deploying.
- Use a payment provider for real transactions. This demonstration project
  must not store card numbers or CVVs in its database.

## Deployment note

`DEBUG = True` and the in-source Django secret key are appropriate only for
local development. Configure environment-based secrets, allowed hosts,
database credentials, HTTPS, and a production static-file strategy before
deploying.
