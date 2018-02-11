# LiveLyrics

LiveLyrics is a web application used to display spotify lyrics in real time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The following python libraries are needed to run this application.

```
pip install flask flask-sqlalchemy flask-migrate pymysql flask-script
```

### Setting up Dev Environment
    1. Clone this repo
    2. Run 'pip install flask flask-sqlalchemy flask-migrate pymysql flask-script'
    3. Run 'export FLASK_CONFIG=development'
    4. Run 'export FLASK_APP=run.py'
    5. Run 'flask run'

### Modifying the Database
    1. Modify 'models.py'
    2. Run 'python manage.py db migrate' to create a migration file
    3. Run 'python manage.py db upgrade' to update the database

## Running the tests

    TODO

## Deployment

    TODO



