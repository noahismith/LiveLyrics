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
    2. Run 'pip install flask flask-sqlalchemy flask-migrate pymysql flask-script alembic requests'
    3. Run 'export FLASK_CONFIG=development'
    4. Run 'export FLASK_APP=run.py'
    5. Run 'flask run'

### Modifying the Database
    1. Modify 'models.py'
    2. Run 'python manage.py db migrate' to create a migration file
    3. Run 'python manage.py db upgrade' to update the database

## Running the tests

    Backend Testing
    1. Login using the web application and get the 'access_token' cookie. 
    2. Place the 'access_token' in the variable spotify_access_token at the top of each test script.
    3. Run 'python user_tests.py
    4. Run 'python spotify_tests.py
    5. Run 'python rating_tests.py
    6. Run 'python lyrics_tests.py
    
    Frontend Testing
    1. Ensure the dev environment is setup and running (see Setting up Dev Environment above)
    2. Open a new terminal and run 'npm install cypress --save-dev'
    3. cd into the 'LiveLyrics' folder
    4. run 'node_modules/.bin/cypress open'
    5. Once the Cypress GUI has opened, double click 'testPlan_cases.js' to run the set of tests

## Deployment
    1. Clone this repo
    2. Run 'chmod +x deploy.sh'
    3. Run '/deploy.sh'



