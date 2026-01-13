# family-recipes

Steps necessary for local setup:
- install Python 3.12 or higher
- install latest Django
- setup database 
python manage.py migrate
- populate DB with sample data
python manage.py loaddata initial_data.json
- start server
python manage.py runserver
-> user front-end: http://127.0.0.1:8000/recipes/ 
-> admin front-end: http://127.0.0.1:8000/admin/

To dump your local data into a fixture:
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e admin -e auth.Permission --indent 2 > <your_fixture_name>.json
-> the exclusions are important, otherwise you get IntegrityErrors when loading the data
